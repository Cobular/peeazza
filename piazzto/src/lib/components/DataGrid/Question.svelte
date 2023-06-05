<script lang="ts">
	import type { Snippet } from "../../typescript/types";

  export let question: Snippet
</script>

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
        on:click
      >
        🍕
      </button>
    {/if}
  </td></tr
>