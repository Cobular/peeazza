<script lang="ts">
	interface Snippet {
		// A number between 0 and 1 representing the rating of the question
		bot_confidence: number;
		snippet_text: string;
		full_text: string;
		post_id: number;
	}

	let active_question: number | undefined = undefined;

	let questions: Snippet[] = [];

	async function getQuestions() {
		const response = await fetch(`http://127.0.0.1:8000/snippets`);
		const data = await response.json();
		console.log(data);
		questions = data;
	}

	getQuestions();
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

<div class="grid grid-cols-[minmax(200px,_2fr)_5fr] gap-3 h-full">
	<div class="bg-base-200 rounded-md">
		<div class="h-1 rounded-t-md bg-base-300" />
		<table class="table">
			<thead class="bg-base-300 rounded-t-md">
				<tr>
					<th>Question</th>
					<th class="cursor-pointer">Confidence</th>
					<th>Action</th>
				</tr>
			</thead>
			<tbody>
				{#each questions as question}
					<tr class="hover">
						<td>
							{question.snippet_text}
						</td>
						<td
							><div
								class="h-2.5 w-2.5 ml-4 rounded-full {question.bot_confidence > 0.8
									? 'bg-emerald-500'
									: question.bot_confidence > 0.5
									? 'bg-yellow-500'
									: question.bot_confidence > 0.4
									? 'bg-red-500'
									: 'bg-green-500'} mr-2"
							/></td
						>
						<!-- if the confidence is 1 then show a button -->
						<td>
							{#if question.bot_confidence === 1}
								<button class="btn btn-sm btn-ghost" on:click={() => console.log('Answered')}>
									Answer
								</button>
							{/if}
						</td></tr
					>
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
