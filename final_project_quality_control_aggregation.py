import pandas as pd
import csv

def majority_vote(mturk_res):
    responses = list(zip((mturk_res['Input.pair1_ai_lyric'].tolist()),(mturk_res['Input.pair1_turker_lyric'].tolist()), (mturk_res['Answer.pair1'].tolist()),(mturk_res['Input.pair2_ai_lyric'].tolist()),(mturk_res['Input.pair2_turker_lyric'].tolist()), (mturk_res['Answer.pair2'].tolist()), (mturk_res['Input.pair3_ai_lyric'].tolist()),(mturk_res['Input.pair3_turker_lyric'].tolist()), (mturk_res['Answer.pair3'].tolist()) ))
    
    l = len(responses)
    pairs = {}
    for i in range(l):
      for j in range(0,len(responses[0]),3):
        curPair = (responses[i][j], responses[i][j+1])
        curAiVote = 1 if (responses[i][j+2] == 'lyric1') else 0
        curTurkVote = 0 if (responses[i][j+2] == 'lyric1') else 1
        if (curPair in pairs):
          (aiVotes, turkVotes) = pairs[curPair]
          votes = (aiVotes + curAiVote, turkVotes + curTurkVote)
          pairs[curPair] = votes
        else:
          votes = (curAiVote, curTurkVote)
          pairs[curPair] = votes
    print(pairs)
    
    ans = []

    for pair in pairs.keys():
      (aiLyr, TurkLyr) = pair
      
      (aiVotes, turkerVotes) = pairs[pair]
      winner = 'AI' if aiVotes > turkerVotes else 'Turker'
      ans.append((aiLyr, TurkLyr, aiVotes, turkerVotes, winner))
    
    ans.sort(key=lambda tup: (tup[0], tup[1]))
    print(ans)
    return ans


def select_qualified_worker(mturk_res_hit2):
    WIds = mturk_res_hit2['worker_id'].tolist()
    QCs = list(zip(WIds,(mturk_res_hit2['Answer.neg_qual_ctrl'].tolist()), (mturk_res_hit2['Answer.pos_qual_ctrl'].tolist())))
    WorkerTots = {}
    WorkerCounts = {}
    
    for i in range(len(QCs)):
      #print("outer")
      worker = QCs[i][0]
      negativeCorrect = False
      numPosCorrect = 0
      
      if (worker in WorkerCounts):
        WorkerCounts[worker] += 1
      else:
        WorkerCounts[worker] = 1

      for j in range(1,len(QCs[1])):

        correct = QCs[i][j] == 'Yes'

        isNan = QCs[i][j] != 'Yes' and QCs[i][j] != 'No' and QCs[i][j] != 'Naa'
        if (j == 1 and not isNan): 
          negativeCorrect = QCs[i][j] != 'Yes'
        if correct and j != 1:
          numPosCorrect += 1
      passed = negativeCorrect and numPosCorrect >= 1
      toAdd = 1 if passed else 0  
      if worker in WorkerTots:
        numPassed = WorkerTots[worker]
        WorkerTots[worker] = numPassed + toAdd
      else:
        WorkerTots[worker] = toAdd

    WIds.sort()
    ans = []
    for w in WIds:
      numPassed = WorkerTots[w]
      numHits = WorkerCounts[w]
      percentage = numPassed/numHits
      if (percentage >= 0.66 and numHits >= 3):
        ans.append((w, round(percentage,3)))

    return ans

def select_coherent_sentences(mturk_res_hit2, sqw):
    
    WIds = mturk_res_hit2['worker_id'].tolist()
    QCs = list(zip(WIds,(mturk_res_hit2['Input.lyric_1'].tolist()), (mturk_res_hit2['Answer.lyric_1'].tolist()) , (mturk_res_hit2['Input.lyric_2'].tolist()), (mturk_res_hit2['Answer.lyric_2'].tolist()) , (mturk_res_hit2['Input.lyric_3'].tolist()), (mturk_res_hit2['Answer.lyric_3'].tolist()), (mturk_res_hit2['Input.lyric_4'].tolist()) , (mturk_res_hit2['Answer.lyric_4'].tolist())))
    ans = []

    for i in range(len(QCs)):
      #print("outer")
      worker = QCs[i][0]
      if [item for item in sqw if item[0] == worker] :
        for j in range(1,len(QCs[1]), 2):
          if QCs[i][j+1] == 'Yes':
            ans.append(QCs[i][j])

    
    return ans

def main():
    # Read in CVS result file with pandas
    # PLEASE DO NOT CHANGE
    mturk_res_hit2 = pd.read_csv('Final_project_data_second_Hit.csv')
    
    mturk_res_hit3 = pd.read_csv('Final_project_data_third_Hit.csv')

    sqw = select_qualified_worker(mturk_res_hit2)
    with open('QC_Workers','w') as out:
      csv_out=csv.writer(out)
      csv_out.writerow(['worker_id', 'percentage'])
      csv_out.writerows(sqw)

    cs = select_coherent_sentences(mturk_res_hit2, sqw)
    df = pd.DataFrame(cs)
    df.to_csv('CoherentTurkerLyrics.csv', index=False)

    mv = majority_vote(mturk_res_hit3)
    with open('LyricVotes','w') as out:
      csv_out=csv.writer(out)
      csv_out.writerow(['AI_lyric', 'TurkerLyric', 'AI_votes', 'Turker_votes', 'Winner'])
      csv_out.writerows(mv)


if __name__ == '__main__':
    main()
