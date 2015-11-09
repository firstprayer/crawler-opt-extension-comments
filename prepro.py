import sys, json

def main():
	fs = open('comments.txt', 'w')
	SPLITER = 'Comment Submitted by '
	cnt = 0
	for l in open(sys.argv[1]):
		if l.endswith('\n'):
			l = l[: -1]
		if not l:
			continue

		texts = json.loads(l)
		# print len(texts)
		idx = 0
		while idx < len(texts):
			curr_line = texts[idx]

			if curr_line.find(SPLITER) >= 0:
				# print cnt, idx, curr_line
				name = curr_line[curr_line.find(SPLITER) + len(SPLITER): ]
				prev_idx = idx - 1
				# while len(texts[prev_idx].split(' ')) < 2:
				# 	prev_idx -= 1
				comment = texts[prev_idx]

				prev_idx -= 1
				# Find the id of this comment.
				id = None
				while prev_idx >= 0:
					prev_line = texts[prev_idx]
					if prev_line.startswith('ICEB-2015'):
						id = prev_line
						break

					if prev_line.find(SPLITER) > 0:
						print "Cannot find id for", name

					prev_idx -= 1

				if id:
					fs.write(json.dumps({'name': name, 'comment': comment, 'id': id}))
					fs.write('\n')
				else:
					print "Cannot find id for", name

			idx += 1

		cnt += 1
		if cnt % 100 == 0:
			print cnt

	fs.close()

if __name__ == '__main__':
	main()