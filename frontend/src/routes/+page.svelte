<script lang="ts">
	import { onMount } from "svelte";
	import ProfileCard from "./ProfileCard.svelte";

	interface WorkExperience {
		location: string;
		company: string;
		role: string;
		start_date: string;
	}

	interface Study {
		school_name: string;
		degree_name: string;
		is_active: boolean;
	}

	interface Skill {
		name: string;
	}

	interface Connection {
		name: string;
		location: string;
		job_title: string;
	}

	interface Profile {
		url: string;
		first_name: string;
		last_name: string;
		current_function: string;
		work_experiences: WorkExperience[];
		studies: Study[];
		skills: Skill[];
		connections: Connection[];
	}

	let profiles: Profile[] = []
	onMount(async () => {
		try {
			const res = await fetch('http://localhost:8000/api/linkedin/profiles')
			profiles = await res.json()
			console.log(profiles)
		} catch (err) {
			console.error(err)
		}
		
	})
</script>

<svelte:head>
	<title>Reshark Linkedin opdracht</title>
	<meta name="description" content="Reshark Opdracht" />
</svelte:head>

<div class="text-white mt-5">
	{#if profiles.length == 0}
		<h1 class="text-2xl py-10 text-center">
			No profiles found, add them on the 
			<a class="underline text-secondary" href="/csv">csv page</a>
		</h1>
	{:else}
		<!-- Load Profiles -->
		<div class="grid lg:grid-cols-4 md:grid-cols-2 grid-cols-1 w-full gap-5">
			{#each profiles as {first_name, last_name, current_function, skills, work_experiences, studies, connections}}
				<ProfileCard 
					{first_name} 
					{last_name} 
					{current_function} 
					{skills} 
					{work_experiences} 
					{studies}
					{connections}
				/>
			{/each}
		</div>
	{/if}
</div>