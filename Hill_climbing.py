#Đồ thị cây của chương trình
graph = {
        'A': ['B', 'C', 'D'],
        'B': ['E'],
        'C': ['E','F'],
        'E': ['G'],
        'F': ['G'],
        'G': ['H'],
        'D': ['H'],
        'H': []
        }
#Hàm đánh giá tại mỗi nút
heuristic = {
        'A': 30,
        'B': 20,
        'C': 10,
        'D': 25,
        'E': 13,
        'F': 15,
        'G': 18,
        'H': 0,
            }
def Hill_Climbing(graph, start, end):
    #Tạo 1 list open
    open = []
    #Đặt điểm start vào trong open
    open.append(start)
    while open:
        #Lấy đường đi dầu tiên trong ngăn xếp
        path = open.pop(0)
        #Lấy ra vị trí cuối cùng trong đường đi
        node = path[-1]
        #In ra đường đi đã tìm thấy
        print(node)
        #Kết thúc chương trình nếu tìm thấy nút con
        if node == end:
            return path
        #Lưu các nút kề với nút đang xét
        child = graph.get(node,[])
        #Sắp xếp các nút con theo thứ tự tăng dần của hàm đánh giá để đưa vào open
        for i in range(0,len(child)-1):
            for j in range(i+1,len(child)):
                if(heuristic[child[i]]<heuristic[child[j]]):      
                    a=child[i]
                    child[i]=child[j]
                    child[j]=a
        for each_child in child:
            new_path = list(path)
            new_path.append(each_child)
            open.insert(0,new_path)
    return "Không tìm thấy đường đi"

#Phần main của bài
#Người dùng nhập vào dữ liệu cho điểm bắt đầu và điểm kết thúc
start = (input("Nhập điểm bắt đầu: "))
start = start.upper()
while start not in graph:
    print("Điểm bắt đầu phải có trong cây!")
    start = input("Nhập lại điểm bắt đầu: ")
    start = start.upper()
end = input("Nhập điểm cần đến: ")
end = end.upper()
while end not in graph:
    print("Điểm đến phải có trong cây!")
    end = input("Nhập lại điểm cần đến: ")
    end = end.upper()
#Gọi hàm
print(Hill_Climbing(graph,start,end))
