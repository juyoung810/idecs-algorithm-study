n = int(input())
ans = []
for _ in range(n):
  k = int(input())
  arr = []
  for _ in range(2):
    arr.append(list(map(int,input().split())))
  #길이가 1일때( k == 1)
  if k == 1:
    ans.append(max(arr[0][0],arr[1][0]))
  else:
    arr[0][1] += arr[1][0]
    arr[1][1] += arr[0][0]
    for i in range(2,k):
      arr[0][i] += max(arr[1][i-1],arr[1][i-2])
      arr[1][i] += max(arr[0][i-1],arr[0][i-2])
    ans.append(max(arr[0][k-1],arr[1][k-1]))

for j in ans:
  print(j)