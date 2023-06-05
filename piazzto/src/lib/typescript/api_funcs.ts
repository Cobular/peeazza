import type { BotResponse, Questions } from './types';

export async function getQuestions(): Promise<Questions> {
	const response = await fetch(`http://127.0.0.1:8000/snippets`);
	const data = await response.json();
	return data;
}

export async function postResponse(bot_response_id: string, post_id: string) {
	const response = await fetch(
		`http://127.0.0.1:8000/bot_responses/post/${post_id}/${bot_response_id}`
	);
	const data = await response.json();
	console.log(data);
}

export async function getResponses(postId: string): Promise<BotResponse[]> {
	const response = await fetch(`http://127.0.0.1:8000/bot_responses/${postId}`);
	const data = await response.json();
	return data;
}
