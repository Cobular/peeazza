<script lang="ts">
	import { parse } from 'postcss';

	export let data;

	interface Snippet {
		// A number between 0 and 1 representing the rating of the question
		bot_confidence: number;
		snippet_text: string;
		full_text: string;
		logs: string;
		post_id: string;
	}

	interface BotResponse {
		bot_response: string;
		bot_response_id: string;
		post_id: string;
		generation_time: string;
	}

	let active_question: Snippet | undefined = undefined;

	let active_text: string | undefined = undefined;

	let questions: Snippet[] = [];

	questions = data.questions;

	let responses: BotResponse[] = [];

	async function getQuestions() {
		const response = await fetch(`http://127.0.0.1:8000/snippets`);
		const data = await response.json();
		questions = data;
	}

	async function postResponse(bot_response_id: string, post_id: string) {
		const response = await fetch(`http://127.0.0.1:8000/bot_responses/post/${post_id}/${bot_response_id}`);
		const data = await response.json();
		console.log(data);
	}

	async function getResponses(postId: string) {
		const response = await fetch(`http://127.0.0.1:8000/bot_responses/${postId}`);
		const data = await response.json();
		responses = data;
	}
</script>

<div class="grid grid-cols-3 gap-3 h-full">
	<div class="navbar bg-base-300 rounded-md col-span-3">
		<a class="btn btn-ghost text-xl uppercase" href="/">Piazzto</a>
		<div class="join ml-auto">
			<select class="select join-item max-w-xs">
				<option disabled selected>Choose a class</option>
				<option>Han Solo</option>
				<option>Greedo</option>
			</select>
		</div>
	</div>

	<div class="bg-base-200 rounded-md h-100 overflow-scroll">
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
							<p class="text-zinc-500">{JSON.parse(question.logs)[0]["t"]}</p>
						</td>
						<td
							><div
								class="h-2.5 w-2.5 ml-4 rounded-full {question.bot_confidence > 0.8
									? 'bg-emerald-500'
									: question.bot_confidence > 0.5
									? 'bg-yellow-500'
									: question.bot_confidence > 0.4
									? 'bg-red-500'
									: 'bg-red-500'} mr-2"
							/></td
						>
						<!-- if the confidence is 1 then show a button -->
						<td>
							{#if question.bot_confidence === 1}
								<button
									class="btn btn-sm btn-ghost"
									on:click={() => {
										active_question = question;
										active_text = question.full_text;
										getResponses(active_question.post_id);
									}}
								>
									🍕
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
	<div class="bg-base-200 rounded-md p-5 col-span-2 h-100 overflow-scroll">
		<p class="text-2xl mb-5">Question Text</p>
		<div class="rounded-lg p-5 bg-base-100">
			{@html active_text}
		</div>
		<div class="divider" />
		<!-- make a card for each response -->
		<p class="text-2xl mb-5">Bot Responses</p>
		{#each responses as response, i}
			<div class="card bg-base-100 shadow-xl w-100 mb-5">
				<div class="card-body">
					<p class="card-title">Response {i + 1}</p>
					<p class="text-zinc-500">generated on {response.generation_time}</p>
					<p>{response.bot_response}</p>
					<div class="card-actions justify-end">
						<button class="btn btn-primary" on:click={() => {
							postResponse(response.bot_response_id, response.post_id);
						}}>Post</button>
					</div>
				</div>
			</div>
		{/each}
		<div class="divider" />
		<p class="text-2xl mb-5">Logs</p>
		<div class="mockup-code">
			{#if active_question}
				{#each JSON.parse(active_question.logs) as line}
					<pre data-prefix=">"><code>{line.n} @ {line.t}</code></pre>
				{/each}
			{/if}
		</div>
	</div>
</div>
