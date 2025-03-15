def getTotalRequests(servers, replacedIds, newIds):
    m, res, total = {}, [], 0
    for i, v in enumerate(servers):
        total += v
        if v not in m:
            m[v] = [i]
        else:
            m[v].append(i)
            
    for i in range(len(replacedIds)):
        oldId = replacedIds[i]
        newId = newIds[i]
        print(m)
        if oldId in m:
            oldServers = m[oldId]
            if newId in m:
                m[newId].extend(oldServers)
            else:
                m[newId] = oldServers
            total -= (len(oldServers)*oldId)
            total += (len(oldServers)*newId)
            m.pop(oldId, None)
            res.append(total)
        else:
            res.append(total)
    return res


servers = [ 9986,  9983, 9998, 9991, 9984, 9995 ] # [2, 5, 2]
replacedIds= [9983, 9981, 9984, 9986, 9986, 9991 ]
newIds = [ 9981, 9991, 9995, 9986, 9992, 9990 ]

result = getTotalRequests(servers, replacedIds, newIds)

print(f"Result: {result}")

# print(sum([ 9986,  9983, 9998, 9991, 9984, 9995 ])) 

# 0 [ 9986,  9983, 9998, 9991, 9984, 9995 ] - 59937

# 1 [ 9986,  9981, 9998, 9991, 9984, 9995 ] - 59935
# 2 [ 9986,  9991, 9998, 9991, 9984, 9995 ] - 59945
# 3 [ 9986,  9991, 9998, 9991, 9995, 9995 ] - 59956
# 4 [ 9986,  9983, 9998, 9991, 9984, 9995 ] - 59956
# 5 [ 9992,  9983, 9998, 9991, 9984, 9995 ] - 59962
# 6 [ 9986,  9983, 9998, 9991, 9984, 9995 ] - 59961