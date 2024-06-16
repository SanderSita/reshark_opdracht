<script>
	import { page } from '$app/stores';
</script>

<header class="w-full flex justify-between p-8 rounded-full border border-grayaccent text-white">
	<div class="">
		<p class="text-xl font-semibold">
			<a href="/">Re:Shark Opdracht</a>
		</p>
	</div>

	<ul class="flex gap-10 text-lg">
		<li class="flex items-center hover:underline" aria-current={$page.url.pathname === '/' ? 'page' : undefined}>
			<a href="/">Profiles</a>
		</li>
		<li class="flex items-center hover:underline" aria-current={$page.url.pathname === '/csv' ? 'page' : undefined}>
			<a href="/csv">CSV</a>
		</li>
	</ul>
	
</header>
