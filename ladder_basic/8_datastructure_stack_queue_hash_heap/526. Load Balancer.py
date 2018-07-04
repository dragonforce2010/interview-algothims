'''
Implement a load balancer for web servers. It provide the following functionality:

Add a new server to the cluster => add(server_id).
Remove a bad server from the cluster => remove(server_id).
Pick a server in the cluster randomly with equal probability => pick().
Example
At beginning, the cluster is empty => {}.

add(1)
add(2)
add(3)
pick()
>> 1         // the return value is random, it can be either 1, 2, or 3.
pick()
>> 2
pick()
>> 1
pick()
>> 3
remove(1)
pick()
>> 2
pick()
>> 3
pick()
>> 3
'''
class LoadBalancer:
    
    def __init__(self):
        self.server_ids = []
        self.id2index = {}

    # @param {int} server_id add a new server to the cluster 
    # @return nothing
    def add(self, server_id):
        if server_id in self.id2index:
            return
        self.server_ids.append(server_id)
        self.id2index[server_id] = len(self.server_ids) - 1

    # @param {int} server_id remove a bad server from the cluster
    # @return nothing
    def remove(self, server_id):
        if server_id not in self.id2index:
            return
        
        # remove the server_id
        index = self.id2index[server_id]
        del self.id2index[server_id]
        
        # overwrite the one to be removed
        last_server_id = self.server_ids[-1]
        self.id2index[last_server_id] = index
        self.server_ids[index] = last_server_id
        self.server_ids.pop()

    # @return {int} pick a server in the cluster randomly with equal probability
    def pick(self):
        import random
        index = random.randint(0, len(self.server_ids) - 1)
        return self.server_ids[index]

'''
难点分析：

随机删除让我们想到可以构建一个数组下标的随机数，然后随机删除数组中的元素，所以我们决定使用数组来存储serverId
删除部分是一个难点，对于删除数组中的某个元素，我们想避免因为删除所带来的大量元素的移动，所以我们可以借鉴堆删除的技巧。我们用数组的最后一个元素替换要删除的元素，然后删除数组的最后一个元素，这样删除总是发生在数组的末尾
查询时，我们还需要根据server的id查找其在数组中的下标的位置，所以我们决定使用字典来实现[]
删除时我们不仅要删除数组元素，还要删除字典中的键以及更新字典中的键
'''