<script lang="ts">

	let file: File | null = null;
	let fileInput: HTMLInputElement | null = null;
	let isLoading: boolean;

	function handleFileChange(e: Event) {
		const input = e.target as HTMLInputElement;
		if (input.files && input.files.length > 0) {
			file = input.files[0];
			console.log(file);
		} else {
			file = null;
		}
	}

	function clickFileInput() {
		if (fileInput) {
			fileInput.click();
		}
	}

	async function uploadCsv() {
		if(!fileInput || !fileInput.files || fileInput.files.length == 0) return;

		isLoading = true;
		let formData = new FormData();
		formData.append('csv_file', fileInput.files[0]);

		try {
			const res = await fetch('http://localhost:8000/api/linkedin/profile/csv', {
				method: 'POST',
				body: formData
			})
			const data = await res.json();

			isLoading = false;
			file = null;
			alert('Profiles succesfully scraped')
		} catch (error) {
			console.log(error)
			alert("something went wrong uploading the csv")
		}
	}
</script>

<svelte:head>
	<title>Upload CSV</title>
	<meta name="description" content="csv pagina" />
</svelte:head>

<div class="w-full flex justify-center">
	<div class="text-white mt-5 flex justify-center flex-col w-1/2 gap-2 text-center">
		<div class="p-5 border-dotted border-secondary w-full">
			<h2 class="text-xl">Upload new Linkedin profiles using a CSV</h2>
			<button on:click={clickFileInput} class="p-2 bg-secondarydark text-white rounded-full mt-2">Choose a file</button>
			<p>{file ? file.name : ''}</p>
		</div>

		<input class="hidden" bind:this={fileInput} accept=".csv" type="file" on:change={handleFileChange} />
	
		<button on:click={uploadCsv} class="bg-secondary px-5 py-3 rounded-full font-bold disabled:bg-secondarydark" disabled={isLoading}>{isLoading ? 'Uploading CSV...' : 'Upload CSV'}</button>
	</div>
</div>
