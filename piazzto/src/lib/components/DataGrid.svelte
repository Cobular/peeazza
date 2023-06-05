<script lang="ts">
	import Questions from "./DataGrid/Questions.svelte";

  let active_text: string;
  let responses: any[];
  let active_question: any;
</script>

<div class="bg-base-200 rounded-md h-100 overflow-scroll">
  <Questions {questions} />
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