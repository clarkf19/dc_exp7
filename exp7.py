# ======================== CSV FILE: WHAT YOU HAVE TO DO ========================
# 1. In VS Code, create a NEW FILE in the SAME folder as this .py file.
# 2. Name it  exp7.csv
# 3. Copy the lines below into it (WITHOUT the '# ' at the start), save with Ctrl+S.
#
#    node_id,is_alive,is_current_coordinator
#    1,TRUE,FALSE
#    2,TRUE,FALSE
#    3,TRUE,FALSE
#    4,TRUE,FALSE
#    5,FALSE,TRUE
#
# RULES: write the nodes in order (1, 2, 3 ...). Use capitals TRUE / FALSE.
#        Make the highest node FALSE, TRUE  (the leader that crashed).
#
# 4. Change DOMAIN below to your chit's domain.   5. Run:  python exp7.py
# ===============================================================================

# BULLY ELECTION
# The leader crashed. Each alive node (smallest first) sends ELECTION to all
# BIGGER nodes. Alive bigger nodes reply OK. The biggest alive node gets no OK,
# so it wins and sends COORDINATOR to everyone.

import csv

DOMAIN = "TrustMesh: Blockchain-Enabled Trusted IoT Framework"   # change to your chit
FILE = "exp7.csv"

nodes = []           # all node ids, e.g. [1, 2, 3, 4, 5]
alive = {}           # e.g. alive[5] = "FALSE"
alive_nodes = []     # only the alive ones, e.g. [1, 2, 3, 4]

for row in csv.DictReader(open(FILE)):
    n = int(row["node_id"])
    nodes.append(n)
    alive[n] = row["is_alive"]
    if alive[n] == "TRUE":
        alive_nodes.append(n)
    if row["is_current_coordinator"] == "TRUE":
        old_leader = n

winner = max(alive_nodes)            # the biggest alive node will win

print("=== Bully Election for", DOMAIN, "===")
print()
print("Coordinator Node", old_leader, "has FAILED")
print()

# every alive node takes a turn, smallest first
for starter in alive_nodes:
    print("Node", starter, "starts ELECTION")
    for n in nodes:
        if n > starter:                          # only send to BIGGER nodes
            print("   Node", starter, "sends ELECTION to Node", n)
            if alive[n] == "TRUE":
                print("   Node", n, "replies OK")
            else:
                print("   Node", n, "does not reply (dead)")
    print()

print("Node", winner, "got no OK, so it is the new leader")
for n in alive_nodes:
    if n != winner:
        print("   Node", winner, "sends COORDINATOR to Node", n)