<script lang="ts">
	import { parse } from 'postcss';
	import Header from '../lib/components/Header.svelte';
	import type { BotResponse, Snippet } from '../lib/typescript/types';
	import DataGrid from '../lib/components/DataGrid.svelte';
	import { getQuestions } from '../lib/typescript/api_funcs';

	let active_question: Snippet | undefined = undefined;

	let active_text: string | undefined = undefined;

	let questions: Snippet[] = [];

	questions = data.questions;

	let responses: BotResponse[] = [];

	getQuestions();
</script>

<div class="grid grid-cols-3 gap-3 h-full">
	<Header />

	<DataGrid />
</div>
