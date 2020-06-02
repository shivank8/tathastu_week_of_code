noOfVotes = int(input("Enter the no of votes: "))
votes = []
for i in range(noOfVotes):
    votes.append(input("Enter the name of the Candidate to cast the Vote: "))
vote = []
for name in votes:
    vote.append((name, votes.count(name)))