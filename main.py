import gpt
from config import get_logger
from datetime import datetime

try:
    logger = get_logger(__file__, 'log_info.log')
except:
    logger = get_logger("---SEM ARQUIVO---", 'log_info_manual.log')


bot1 = gpt.ChamadoOpenAI(
    model = "gpt-4-1106-preview",
    assistant_instructions= """
        You are an assistant that has studied and is well versed in macroeconomics. Your main object of study is the keynesian branch of macroeconomics.
        You are very passionate about your knowledge and beliefs about Keynes's thoughts, but you also know that it is not a complete theory and you can be persuaded to change some of your beliefs.
        Your aim is to defend your point of view against different macroeconomic views, specially against Austrian school of economics.
        """
)
logger.info(f"Criado Bot 1")

bot2 = gpt.ChamadoOpenAI(
    model = "gpt-4-1106-preview",
    assistant_instructions= """
        You are an assistant that has studied and is well versed in macroeconomics. Your main object of study is the Hayek's branch of macroeconomics.
        You are very passionate about your knowledge and beliefs about Hayek's thoughts, but you also know that it is not a complete theory and you can be persuaded to change some of your beliefs.
        Your aim is to defend your point of view against different macroeconomic views, specially against keynesian school of economics.
        """
)
logger.info(f"Criado Bot 2")

points_of_view = {
    'bot1':'keynesian macroeconomics',
    'bot2':"Hayek's macroeconomics"
}

# Dictionary to store the answers
answer = {
    'bot1':f'Please elucidate me with the most important aspects of your thoughts on macroeconomics. Be specific to focus on the view of {points_of_view["bot1"]}',
    'bot2':f'Please elucidate me with the most important aspects of your thoughts on macroeconomics. Be specific to focus on the view of {points_of_view["bot2"]}'
}

num_of_replicas = 20

answers = [answer]
replicas = []

start_time = datetime.now()
for r in range(num_of_replicas):
    logger.info(f"Begin iteration {r}")
    replica_text = {
        'bot1': f'Criticize the following view on macroeconomics according to {points_of_view["bot1"]}: {answers[r]["bot2"]}',
        'bot2': f'Criticize the following view on macroeconomics according to {points_of_view["bot2"]}: {answers[r]["bot1"]}'
    }
    replicas.append(replica_text)

    answer = {
        'bot1': bot1.get_content_from_run(bot1.run(replica_text['bot1'])),
        'bot2': bot2.get_content_from_run(bot2.run(replica_text['bot2']))
    }

    answers.append(answer)
end_time = datetime.now()
time_difference = end_time - start_time

logger.info(f"End of replicas. Total seconds: {time_difference.total_seconds()}")
    
answers[5]['bot1']

    

    