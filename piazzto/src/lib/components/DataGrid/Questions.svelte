<script lang="ts">
	import type { Questions } from "../../typescript/types";
	import Question from "./Question.svelte";
  export let questions: Questions;
</script>
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
      <Question {question} on:click />
      {/each}
    </tbody>
  </table>