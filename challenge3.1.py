def linearSearchProduct (productlist, targetproduct):
    indices = []

    for index, product in enumerate(productlist):
        if product == targetproduct:
            indices.append(index)
    return indices


product = ["shoes","boot","loafer","shoes","sandal","shoes"]
target = "shoes"
target2 = "apple"
result = linearSearchProduct(product,target)
result2 = linearSearchProduct(product,target2)
print(result);
print(result2)