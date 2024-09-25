def dfs_adj_matrix(graph, start_node, visited=None, result=None):
  if visited is None:
    visited = [False] * len(graph)
  if result is None:
    result = []

visited[start_node] = True
result.append(start_node)

for neighbor, is_connected in enumerate(graph[start_node]):
  if is_connected and not visited[neighbor]:
    dfs_adj_matrix(graph, neighbor, visited, result)

return result
