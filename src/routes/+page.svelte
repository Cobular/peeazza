<script lang="ts">
	interface Snippet {
		// A number between 0 and 1 representing the rating of the question
		rating: number;
		content: string;
	}

	let active_question: number | undefined = undefined;

	let questions: Snippet[] = [
		{
			rating: 0.5,
			content: 'How do I use SvelteKit?'
		},
		{
			rating: 0.7,
			content: 'What is the meaning of life?'
		},
		{
			rating: 0.2,
			content: 'What is the airspeed velocity of an unladen swallow?'
		}
	];
</script>

<div class="navbar bg-base-300 rounded-md mb-3">
	<a class="btn btn-ghost text-xl uppercase" href="/">Piazzto</a>
	<div class="join ml-auto">
		<select class="select join-item max-w-xs">
			<option disabled selected>Choose a class</option>
			<option>Han Solo</option>
			<option>Greedo</option>
		</select>
	</div>
</div>

<div class="grid grid-cols-[minmax(150px,_2fr)_5fr] gap-3 h-full">
	<div class="bg-base-200 rounded-md">
    <div class="h-1 rounded-t-md bg-base-300"></div>
		<table class="table">
			<thead class="bg-base-300 rounded-t-md">
				<tr>
					<th>Question</th>
					<th class="cursor-pointer">Score</th>
				</tr>
			</thead>
			<tbody>
				{#each questions as question}
					<tr class="hover">
						<td>
							{question.content}
						</td>
						<td class="font-mono">
							{question.rating}
						</td>
					</tr>
				{/each}
			</tbody>
		</table>
		<!-- <div class="flex flex-col gap-2 p-3">
      {#each questions as question}
      <div class="flex flex-row">
        <h2 class="italic">
          {question.content}
        </h2>
        <code class="ml-auto">
          {question.rating}
        </code>
      </div>
   {/each}
    </div> -->
	</div>
	<div class="bg-blue-500" />
</div>
