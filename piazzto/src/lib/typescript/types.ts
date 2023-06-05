
export interface Snippet {
  // A number between 0 and 1 representing the rating of the question
  bot_confidence: number;
  snippet_text: string;
  full_text: string;
  logs: string;
  post_id: string;
}

export interface BotResponse {
  bot_response: string;
  bot_response_id: string;
  post_id: string;
  generation_time: string;
}

export type Questions = Snippet[];