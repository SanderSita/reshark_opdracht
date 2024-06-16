<script>
	export let first_name;
    export let last_name;
    export let current_function;
    export let skills;
    export let work_experiences;
    export let studies;
    export let connections;

    let showWorkExperience = false;
    let showStudies = false;
    let showConnectins = false;

    function toggleWorkExperience() {
        showWorkExperience = !showWorkExperience;
    }

    function toggleConnections() {
        showConnectins = !showConnectins;
    }

    function toggleStudies() {
        showStudies = !showStudies;
    }
</script>

<div class="p-5 border border-grayaccent rounded-3xl flex flex-col gap-2 hover:border-secondary duration-200">
    <p class="text-xl font-bold">{first_name} {last_name}</p>
    <p class= "text-defaulttext text-md">{current_function}</p>

    <div class="flex gap-2 flex-wrap">
        {#each skills as {name}}
            <div class="rounded-full px-2 bg-secondarydark">
                <span class="text-secondary">{name}</span>
            </div>
        {/each}
    </div>

    <div class="w-full rounded-xl py-2 relative">
        <!-- Show work experiences -->
        {#if work_experiences.length > 0}
            <button on:click={toggleWorkExperience} class="bg-secondarydark text-secondary text-xl w-full py-2 relative flex items-center justify-center {showWorkExperience ? 'rounded-t-2xl' : 'rounded-full'}">
                Work Experience
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-chevron-down absolute right-5 my-auto {showWorkExperience ? 'rotate-180' : ''}" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708"/>
                </svg>
            </button>
        {/if}

        <div class="relative">
            {#if showWorkExperience}
                <div class="absolute bg-secondarydark z-50 rounded-b-xl p-4">
                    {#each work_experiences as {location, company, role, start_date}}
                        <div class="py-2">
                            <p>
                                <span class="font-semibold">location: </span>
                                <span>{location}</span>
                            </p>
                            <p>
                                <span class="font-semibold">Company: </span>
                                <span>{company}</span>
                            </p>
                            <p>
                                <span class="font-semibold">Role: </span>
                                <span>{role}</span>
                            </p>
                            <p>
                                <span class="font-semibold">Start Date: </span>
                                <span>{start_date}</span>
                            </p>
                        </div>
                    {/each}
                </div>
            {/if}
        </div>

        <!-- Show Connections -->
        {#if connections.length > 0}
            <button on:click={toggleConnections} class="bg-secondarydark text-secondary text-xl w-full py-2 mt-2 relative flex items-center justify-center {showConnectins ? 'rounded-t-2xl' : 'rounded-full'}">
                Connections
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-chevron-down absolute right-5 my-auto {showConnectins ? 'rotate-180' : ''}" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708"/>
                </svg>
            </button>
        {/if}

        <div class="relative">
            {#if showConnectins}
                <div class="absolute bg-secondarydark z-50 rounded-b-xl p-4">
                    {#each connections as {name, job_title, location}}
                        <div class="py-2">
                            <p>
                                <span class="font-semibold">name: </span>
                                <span>{name}</span>
                            </p>
                            <p>
                                <span class="font-semibold">Job title: </span>
                                <span>{job_title}</span>
                            </p>
                            <p>
                                <span class="font-semibold">location: </span>
                                <span>{location}</span>
                            </p>
                        </div>
                    {/each}
                </div>
            {/if}
        </div>

        <!-- Show Studies -->
        {#if studies.length > 0}
            <button on:click={toggleStudies} class="bg-secondarydark text-secondary text-xl w-full py-2 mt-2 relative flex items-center justify-center {showStudies ? 'rounded-t-2xl' : 'rounded-full'}">
                Studies
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-chevron-down absolute right-5 my-auto {showStudies ? 'rotate-180' : ''}" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708"/>
                </svg>
            </button>
        {/if}

        <div class="relative">
            {#if showStudies}
                <div class="absolute bg-secondarydark z-50 rounded-b-xl p-4">
                    {#each studies as {degree_name, is_active, school_name}}
                        <div class="py-2">
                            <p>
                                <span class="font-semibold">Degree: </span>
                                <span>{degree_name}</span>
                            </p>
                            <p>
                                <span class="font-semibold">School name: </span>
                                <span>{school_name}</span>
                            </p>
                            <p>
                                <span class="font-semibold">Active: </span>
                                <span>{is_active ? 'Yes' : 'No'}</span>
                            </p>
                        </div>
                    {/each}
                </div>
            {/if}
        </div>
    </div>
</div>