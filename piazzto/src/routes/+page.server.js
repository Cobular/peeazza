/** @type {import('./$types').PageServerLoad} */
export async function load({ params }) {
    async function getQuestions() {
		const response = await fetch(`http://127.0.0.1:8000/snippets`);
		const questionsData = await response.json();

        return questionsData;
	}

    return {
        questions: await getQuestions(),
    };
}