from django.http import JsonResponse
import csv
from ninja import Router
from linkedin.models import Connection, Profile, Skill, Study, WorkExperience
from .linkedin import get_profile, get_profile_connections

linkedin_router = Router()

# get array of urls
# get the id from the url
# execute the 2 api functions, get the data
# insert the data in the db
@linkedin_router.post("/profile/csv")
def upload_csv(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            return JsonResponse({'error': 'Invalid file format. Please upload a CSV file.'}, status=400)
        
        urls = []
        # Get URLs from csv
        try:
            # Decode csv file, Django reads in bytes by default
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            csv_reader = csv.reader(decoded_file)
            for row in csv_reader:
                # Get urls from first collumn
                if row:
                    urls.append(row[0])
                    
        except csv.Error:
            return JsonResponse({'error': 'Error reading the CSV file.'}, status=500)
        
        for url in urls:
            # Delete existing profile if exists
            existing_profile = Profile.objects.filter(url=url).first()
            if existing_profile:
                existing_profile.delete()
            
            split_array = url.split('/')
            profile_id = split_array[len(split_array) - 2]
            
            profile_data = get_profile(profile_id)
            connections_data = get_profile_connections(profile_id)
            
            first_name = profile_data.get('firstName', '')
            last_name = profile_data.get('lastName', '')
            current_function = profile_data.get('headline', '')
            experiences_data = profile_data.get('experience', [])
            studies_data = profile_data.get('education', [])
            skills_data = profile_data.get('skills', [])
            
            experiences = []
            for exp in experiences_data:
                date_obj = exp.get('timePeriod').get('startDate')
                month = str(date_obj.get('month', ''))
                year = str(date_obj.get('year', ''))
                start_date = f"{month}-{year}"
                
                new_experience = WorkExperience.objects.create(
                    location = exp.get('locationName', ''),
                    company = exp.get('companyName', ''),
                    role = exp.get('title', ''),
                    start_date = start_date
                )
                experiences.append(new_experience)
            
            studies = []
            for study in studies_data:
                new_study = Study.objects.create(
                    school_name = study.get('school', {}).get('schoolName', ''),
                    degree_name = study.get('degreeName', ''),
                    is_active = study.get('school', {}).get('active', False)
                )
                studies.append(new_study)
            
            skills = []
            for skill in skills_data:
                new_skill = Skill.objects.create(
                    name = skill.get('name', '')
                )
                skills.append(new_skill)
            
            connections = []
            for conn in connections_data:
                new_connection = Connection.objects.create(
                    name = conn.get('name', ''),
                    location = conn.get('location', ''),
                    job_title = conn.get('jobtitle', '')
                )
                connections.append(new_connection)
            
            # Create and save the Profile object
            profile = Profile.objects.create(
                url = url,
                first_name = first_name,
                last_name = last_name,
                current_function = current_function
            )
            
            # Add the data to the profile
            profile.work_experiences.set(experiences)
            profile.studies.set(studies)
            profile.skills.set(skills)
            profile.connections.set(connections)
            profile.save()
            
        return JsonResponse({'message': 'Profiles created successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method or no file uploaded.'}, status=400)

@linkedin_router.get("/profile/{profile_id}")
def profile(request, profile_id: str):
    return get_profile(profile_id)

@linkedin_router.get("/profile/{profile_id}/connections")
def profile_connections(request, profile_id: str):
    return get_profile_connections(profile_id)

@linkedin_router.get("/profiles")
def get_profiles(request):
    profiles = Profile.objects.all().prefetch_related('work_experiences', 'studies', 'skills', 'connections')
    response = []

    for profile in profiles:
        profile_data = {
            'url': profile.url,
            'first_name': profile.first_name,
            'last_name': profile.last_name,
            'current_function': profile.current_function,
            'work_experiences': [
                {
                    'location': exp.location,
                    'company': exp.company,
                    'role': exp.role,
                    'start_date': exp.start_date
                } for exp in profile.work_experiences.all()
            ],
            'studies': [
                {
                    'school_name': study.school_name,
                    'degree_name': study.degree_name,
                    'is_active': study.is_active
                } for study in profile.studies.all()
            ],
            'skills': [
                {
                    'name': skill.name
                } for skill in profile.skills.all()
            ],
            'connections': [
                {
                    'name': conn.name,
                    'location': conn.location,
                    'job_title': conn.job_title
                } for conn in profile.connections.all()
            ]
        }
        response.append(profile_data)
    return response