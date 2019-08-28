def solition(progresses, speeds):
	answer=[]
	success=[]
	count=0
	temp=0
	for i in ragne(0,len(progresses)):
		temp=progresses[i]
		count =0
		while(1):
			if temp >=100:
				break
			else:
				temp+=speeds[i]
				count+=1
		success.append(count)

	temp=0
	count=0
	for j in range(0, len(success)):
		if temp < success[j]:
			if count>0 :
				answer.append(count)
			temp=success[j]
			count=0
			count+=1
		else:
			count+=1
	answer.append(count)
	return answer	