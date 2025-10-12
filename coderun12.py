def main():
    n = int(input())
    
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    start, end = map(int, input().split())

    start = start - 1
    end = end - 1
 
    distances = []
    for i in range(n):
        distances.append(float('infinity'))
    
    distances[start] = 0
    
    visited = []
    for i in range(n):
        visited.append(False)
    
    for iteration in range(n):
        
        closest_city = -1
        shortest_distance = float('infinity')
        
        for city in range(n):
            if visited[city]:
                continue
            
            if distances[city] < shortest_distance:
                shortest_distance = distances[city]
                closest_city = city
        
        if closest_city == -1:
            break
        
        visited[closest_city] = True
        

        for neighbor in range(n):
            if matrix[closest_city][neighbor] == 0:
                continue
            
            new_distance = distances[closest_city] + matrix[closest_city][neighbor]
            
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
    
    if distances[end] == float('infinity'):
        print("Пути не существует")
    else:
        print(distances[end])


if __name__ == '__main__':
    main()