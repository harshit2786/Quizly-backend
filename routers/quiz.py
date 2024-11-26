from fastapi import APIRouter,HTTPException
from schemas import quesion_model
from services.openAI import client

router = APIRouter()

@router.post("/getquiz", response_model=quesion_model.QuestionSet)
async def getquiz(request : quesion_model.QuizRequest):
    """
    Generate a quiz with 10 questions on the given topic.
    """
    try:
        topic = request.topic
        # Call OpenAI API via the client
        response = client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a quiz generator. Generate 10 questions for a quiz."},
                {"role": "user", "content": f"Generate a quiz on the topic: {topic}."},
            ],
            response_format=quesion_model.QuestionSet,
        )

        # Parse response into QuestionSet model
        
        question_set = response.choices[0].message.parsed

        return question_set

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))