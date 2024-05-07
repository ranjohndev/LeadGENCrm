# agents/management/commands/import_leads_data.py

import os
import csv
from django.core.management.base import BaseCommand
from leads.models import Lead, UserProfile

class Command(BaseCommand):
    help = 'Import leads data from CSV file'

    def handle(self, *args, **options):
        csv_file_path = os.path.join('C:\\Users\\New\\leadgencrm\\csv', 'all_barbershop_leads.csv')
        print("CSV File Path:", csv_file_path)
        if not os.path.exists(csv_file_path):
            self.stdout.write(self.style.ERROR('CSV file does not exist'))
            return

        # Assume the username or email of the organisation is in the first column of the CSV file
        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                # Fetch UserProfile based on username or email (adjust as needed)
                organisation_username_or_email = row[0]
                try:
                    organisation_userprofile = UserProfile.objects.get(user__username=organisation_username_or_email)  # Assuming username
                except UserProfile.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'UserProfile with username {organisation_username_or_email} does not exist'))
                    continue

                # Create Lead instance and assign organisation
                lead = Lead.objects.create(
                    organisation=organisation_userprofile,
                    first_name=row[1],  # Assuming second column is first name
                    last_name=row[2],   # Assuming third column is last name
                    # Add other fields as needed
                )
                # Handle other fields and create Lead instance accordingly
                # You need to ensure all mandatory fields are provided

        self.stdout.write(self.style.SUCCESS('Leads data imported successfully'))
