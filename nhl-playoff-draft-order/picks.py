import itertools
from operator import itemgetter

# round 1 participants list of lists
# index 0: team name, index 1: seed, index 2: division winner
r11 = [['DAL', 2, 'y'], ['MIN', 16, 'n']]
r12 = [['STL', 3, 'n'], ['CHI', 5, 'n']]

r13 = [['ANA', 6, 'y'], ['NSH', 14, 'n']]
r14 = [['LAK', 8, 'n'], ['SJS', 11, 'n']]

r15 = [['WSH', 1, 'y'], ['PHI', 13, 'n']]
r16 = [['PIT', 4, 'n'], ['NYR', 9, 'n']]

r17 = [['FLA', 7, 'y'], ['NYI', 10, 'n']]
r18 = [['TBL', 12, 'n'], ['DET', 15, 'n']]

# CARTESIAN PRODUCTS AFTER ROUND 1 PARTICIPANTS FINALIZED
# round 2 participants cartesian product
r21_first = list(itertools.product(r11, r12))
r22_first = list(itertools.product(r13, r14))

r23_first = list(itertools.product(r15, r16))
r24_first = list(itertools.product(r17, r18))

# round 3 (conference finals) participants cartesian product
r31_first = list(itertools.product(r21_first, r22_first))
r32_first = list(itertools.product(r23_first, r24_first))

# round 4 (stanley cup final) participants cartesian product
r41_first = list(itertools.product(r31_first, r32_first))
len_r41_first = len(r41_first) # 256 possibilities for this loop

# round 1 winners and losers
for i in range(0,len_r41_first):
	r11_winner = r41_first[i][0][0][0]
	if r11_winner == r11[0]:
		r11_loser = r11[1]
	else:
		r11_loser = r11[0]

	r12_winner = r41_first[i][0][0][1]
	if r12_winner == r12[0]:
		r12_loser = r12[1]
	else:
		r12_loser = r12[0]

	r13_winner = r41_first[i][0][1][0]
	if r13_winner == r13[0]:
		r13_loser = r13[1]
	else:
		r13_loser = r13[0]

	r14_winner = r41_first[i][0][1][1]
	if r14_winner == r14[0]:
		r14_loser = r14[1]
	else:
		r14_loser = r14[0]

	r15_winner = r41_first[i][1][0][0]
	if r15_winner == r15[0]:
		r15_loser = r15[1]
	else:
		r15_loser = r15[0]

	r16_winner = r41_first[i][1][0][1]
	if r16_winner == r16[0]:
		r16_loser = r16[1]
	else:
		r16_loser = r16[0]

	r17_winner = r41_first[i][1][1][0]
	if r17_winner == r17[0]:
		r17_loser = r17[1]
	else:
		r17_loser = r17[0]

	r18_winner = r41_first[i][1][1][1]
	if r18_winner == r18[0]:
		r18_loser = r18[1]
	else:
		r18_loser = r18[0]

	# index for team name is 0 in round 1 participants list of lists
	name = 0;
	r1_summary = ("r11 winner: " + r11_winner[name] + "\n" +
	              "r12 winner: " + r12_winner[name] + "\n" +
	              "r13 winner: " + r13_winner[name] + "\n" +
	              "r14 winner: " + r14_winner[name] + "\n" +
	              "r15 winner: " + r15_winner[name] + "\n" +
	              "r16 winner: " + r16_winner[name] + "\n" +
	              "r17 winner: " + r17_winner[name] + "\n" +
	              "r18 winner: " + r18_winner[name] + "\n" +
	              "r11 loser: " + r11_loser[name] + "\n" +
	              "r12 loser: " + r12_loser[name] + "\n" +
	              "r13 loser: " + r13_loser[name] + "\n" +
	              "r14 loser: " + r14_loser[name] + "\n" +
	              "r15 loser: " + r15_loser[name] + "\n" +
	              "r16 loser: " + r16_loser[name] + "\n" +
	              "r17 loser: " + r17_loser[name] + "\n" +
	              "r18 loser: " + r18_loser[name])

	# round 2 participants
	r21 = [r11_winner, r12_winner]
	r22 = [r13_winner, r14_winner]
	r23 = [r15_winner, r16_winner]
	r24 = [r17_winner, r18_winner]

	# CARTESIAN PRODUCT AFTER ROUND 2 PARTICIPANTS FINALIZED
	# round 3 (conference finals) participants cartesian product
	r31_second = list(itertools.product(r21, r22))
	r32_second = list(itertools.product(r23, r24))

	# round 4 (stanley cup final) participants cartesian product
	r41_second = list(itertools.product(r31_second, r32_second))
	len_r41_second = len(r41_second) # 16 possibilities for this loop

	# round 2 winners and losers
	for i in range(0,len_r41_second):
		r21_winner = r41_second[i][0][0]
		if r21_winner == r21[0]:
			r21_loser = r21[1]
		else:
			r21_loser = r21[0]

		r22_winner = r41_second[i][0][1]
		if r22_winner == r22[0]:
			r22_loser = r22[1]
		else:
			r22_loser = r22[0]

		r23_winner = r41_second[i][1][0]
		if r23_winner == r23[0]:
			r23_loser = r23[1]
		else:
			r23_loser = r23[0]

		r24_winner = r41_second[i][1][1]
		if r24_winner == r24[0]:
			r24_loser = r24[1]
		else:
			r24_loser = r24[0]

		r2_summary = ("r21 winner: " + r21_winner[name] + "\n" +
		              "r22 winner: " + r22_winner[name] + "\n" +
		              "r23 winner: " + r23_winner[name] + "\n" +
		              "r24 winner: " + r24_winner[name] + "\n" +
		              "r21 loser: " + r21_loser[name] + "\n" +
		              "r22 loser: " + r22_loser[name] + "\n" +
		              "r23 loser: " + r23_loser[name] + "\n" +
		              "r24 loser: " + r24_loser[name])

		# round 3 participants
		r31 = [r21_winner, r22_winner]
		r32 = [r23_winner, r24_winner]

		# CARTESIAN PRODUCT AFTER ROUND 3 PARTICIPANTS FINALIZED
		# round 4 (stanley cup final) participants cartesian product
		r41_third = list(itertools.product(r31, r32))
		len_r41_third = len(r41_third) # 4 possibilities for this loop

		# round 3 winners and losers
		for i in range(0,len_r41_third):
			r31_winner = r41_third[i][0]
			if r31_winner == r31[0]:
				r31_loser = r31[1]
			else:
				r31_loser = r31[0]

			r32_winner = r41_third[i][1]
			if r32_winner == r32[0]:
				r32_loser = r32[1]
			else:
				r32_loser = r32[0]

			r3_summary = ("r31 winner: " + r31_winner[name] + "\n" +
			              "r32 winner: " + r32_winner[name] + "\n" +
			              "r31 loser: " + r31_loser[name] + "\n" +
			              "r32 loser: " + r32_loser[name])

			# round 4 participants
			r41 = [r31_winner, r32_winner]


			# CARTESIAN PRODUCT AFTER ROUND 4 PARTICIPANTS FINALIZED
			# round 4 (stanley cup final) winner cartesian product
			r41_fourth = [r31_winner, r32_winner]
			len_r41_fourth = len(r41_fourth) # 2 possibilities for this loop

			# round 4 winner and loser
			for i in range(0,len_r41_fourth):
				r41_winner = r41_fourth[i]
				if r41_winner == r41[0]:
					r41_loser = r41[1]
				else:
					r41_loser = r41[0]

				r4_summary = ("r41 winner: " + r41_winner[name] + "\n" +
				              "r41 loser: " + r41_loser[name])

				# round 1 and round 2 losers
				r1_r2_losers = [r11_loser, r12_loser, r13_loser, r14_loser,
								r15_loser, r16_loser, r17_loser, r18_loser,
								r21_loser, r22_loser, r23_loser, r24_loser]

				# round 3 losers
				r3_losers = [r31_loser, r32_loser]

				# index for seed is 1 in round 1 participants list of lists
				seed = 1
				if r31_loser[seed] < r32_loser[seed]:
					pick_28 = r31_loser
					pick_27 = r32_loser
				else:
					pick_28 = r32_loser
					pick_27 = r31_loser

				# index for division winner is 2 in round 1 participants list of lists
				div_winner = 2
				div_winners_r1_r2_losers = []
				for team in r1_r2_losers:
					if team[div_winner] == 'y':
						div_winners_r1_r2_losers.append(team)
						r1_r2_losers.remove(team)

				if not div_winners_r1_r2_losers:
					remaining_picks = sorted(r1_r2_losers, key=itemgetter(seed))
				else:
					div_winners_r1_r2_losers = sorted(div_winners_r1_r2_losers, key=itemgetter(seed))
					for team in div_winners_r1_r2_losers:
						remaining_picks.append(team)
					r1_r2_losers = sorted(r1_r2_losers, key=itemgetter(seed))
					for team in r1_r2_losers:
						remaining_picks.append(team)

				draft_order = ("30th: " + r41_winner[name] + "\n" +
							   "29th: " + r41_loser[name] + "\n" +
							   "28th: " + pick_28[name] + "\n" +
							   "27th: " + pick_27[name] + "\n" +
							   "26th: " + remaining_picks[0][name] + "\n" +
							   "25th: " + remaining_picks[1][name] + "\n" +
							   "24th: " + remaining_picks[2][name] + "\n" +
							   "23rd: " + remaining_picks[3][name] + "\n" +
							   "22nd: " + remaining_picks[4][name] + "\n" +
							   "21st: " + remaining_picks[5][name] + "\n" +
							   "20th: " + remaining_picks[6][name] + "\n" +
							   "19th: " + remaining_picks[7][name] + "\n" +
							   "18th: " + remaining_picks[8][name] + "\n" +
							   "17th: " + remaining_picks[9][name] + "\n" +
							   "16th: " + remaining_picks[10][name] + "\n" +
							   "15th: " + remaining_picks[11][name])

				print "ROUND SUMMARIES"
				print "Round 1"
				print r1_summary
				print ""
				print "Round 2"
				print r2_summary
				print ""
				print "Round 3"
				print r3_summary
				print ""
				print "Round 4"
				print r4_summary
				print ""
				print "DRAFT ORDER"
				print draft_order
				print ""
				print "/////////"
				print ""

				# clear lists
				del r1_r2_losers[:]
				del div_winners_r1_r2_losers[:]
				del remaining_picks[:]
