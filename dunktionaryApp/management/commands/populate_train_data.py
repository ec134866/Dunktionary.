# management/commands/populate_train_data.py
from django.core.management.base import BaseCommand
from dunktionaryApp.models import Pass, PassLevel, Dunk, DunkLevel, Variation, TrickScore

class Command(BaseCommand):
    help = 'Populate train-making data from trainmaker.py'

    def handle(self, *args, **options):
        # Import your existing data
        from dunktionaryApp.trainmaker import passes, dunks, scoring_table
        
        self.stdout.write('Clearing existing train data...')
        PassLevel.objects.all().delete()
        DunkLevel.objects.all().delete()
        Variation.objects.all().delete()
        TrickScore.objects.all().delete()
        
        # First, collect ALL unique variation names
        self.stdout.write('Creating variation master list...')
        all_variation_names = set()
        
        for pass_variations in passes.values():
            for pass_details in pass_variations:
                all_variation_names.update(pass_details.get('variations', []))
        
        for dunk_variations in dunks.values():
            for dunk_details in dunk_variations:
                all_variation_names.update(dunk_details.get('variations', []))
        
        # Create Variation objects
        variation_objects = {}
        for var_name in all_variation_names:
            var_obj = Variation.objects.create(name=var_name)
            variation_objects[var_name] = var_obj
        
        self.stdout.write(f'Created {len(variation_objects)} unique variations')
        
        # Populate passes
        self.stdout.write('Populating passes...')
        for pass_name, pass_variations in passes.items():
            # Get or create the Pass object
            pass_obj, created = Pass.objects.get_or_create(
                name=pass_name,
                defaults={'classification': 'Train Pass'}
            )
            
            # Create level records with their specific variations
            for pass_details in pass_variations:
                pass_level = PassLevel.objects.create(
                    pass_ref=pass_obj,
                    level=pass_details['level'],
                    can_start=pass_details.get('can_start', False),
                    can_follow=pass_details.get('can_follow', False)
                )
                
                # Link the variations for this specific level
                for var_name in pass_details.get('variations', []):
                    pass_level.variations.add(variation_objects[var_name])
        
        # Populate dunks
        self.stdout.write('Populating dunks...')
        for dunk_name, dunk_variations in dunks.items():
            # Get or create the Dunk object
            dunk_obj, created = Dunk.objects.get_or_create(
                name=dunk_name,
                defaults={'classification': 'Train Dunk'}
            )
            
            # Create level records with their specific variations
            for dunk_details in dunk_variations:
                dunk_level = DunkLevel.objects.create(
                    dunk_ref=dunk_obj,
                    level=dunk_details['level']
                )
                
                # Link the variations for this specific level
                for var_name in dunk_details.get('variations', []):
                    dunk_level.variations.add(variation_objects[var_name])
        
        # Populate scores
        self.stdout.write('Populating scores...')
        for trick_name, score_value in scoring_table.items():
            TrickScore.objects.create(
                trick_name=trick_name,
                score_value=score_value
            )
        
        self.stdout.write(self.style.SUCCESS(
            f'Successfully populated:\n'
            f'  - {Variation.objects.count()} variations\n'
            f'  - {PassLevel.objects.count()} pass levels\n'
            f'  - {DunkLevel.objects.count()} dunk levels\n'
            f'  - {TrickScore.objects.count()} trick scores'
        ))