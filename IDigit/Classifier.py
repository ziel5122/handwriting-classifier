
def initializeKNNMNIST(num_neighbors):
    from sklearn.neighbors import KNeighborsClassifier
    clf = KNeighborsClassifier(num_neighbors)
    
    from sklearn import datasets
    from sklearn.datasets import fetch_mldata
    dataset = fetch_mldata("MNIST original", data_home="http://mldata.org/repository/data/download/matlab/mnist-original/")  
    clf.fit(dataset.data, dataset.target)
    
    return clf

def initializeKNNMNISTsmall(num_neighbors):
    from sklearn.neighbors import KNeighborsClassifier
    clf = KNeighborsClassifier(num_neighbors)
    
    from sklearn import datasets
    from sklearn.datasets import fetch_mldata
    dataset = fetch_mldata("MNIST original", data_home="http://mldata.org/repository/data/download/matlab/mnist-original/")  
    
    data = dataset.data.reshape((len(dataset.data), -1))
    
    subset_data = []
    subset_target = []
    
    for i in range(0, 180):
        subset_data.append(data[i])
        subset_target.append(dataset.target[i])
    
    for i in range(5923, 6103):
        subset_data.append(data[i])
        subset_target.append(dataset.target[i])
        
    for i in range(12665, 12845):
        subset_data.append(data[i])
        subset_target.append(dataset.target[i])
    
    for i in range(18623, 18803):
        subset_data.append(data[i])
        subset_target.append(dataset.target[i])
    
    for i in range(24754, 24754+180):
        subset_data.append(data[i])
        subset_target.append(dataset.target[i])
    
    for i in range(30596, 30596+180):
        subset_data.append(data[i])
        subset_target.append(dataset.target[i])
        
    for i in range(36017, 36017+180):
        subset_data.append(data[i])
        subset_target.append(dataset.target[i])
        
    for i in range(41935, 41935+180):
        subset_data.append(data[i])
        subset_target.append(dataset.target[i])
        
    for i in range(48200, 48200+180):
        subset_data.append(data[i])
        subset_target.append(dataset.target[i])
        
    for i in range(54051, 54051+180):
        subset_data.append(data[i])
        subset_target.append(dataset.target[i])
    
    clf.fit(subset_data, subset_target)

    return clf

def initializeClassifier(num_neighbors):
    from sklearn import datasets
    digits = datasets.load_digits()
    
    n_samples = len(digits.images)
    data = digits.images.reshape((n_samples, -1))
    
    from sklearn.neighbors import KNeighborsClassifier
    clf = KNeighborsClassifier(n_neighbors = num_neighbors)
    clf.fit(data, digits.target)
    
    return clf
    

def make1D(image_matrices):
    X.reshape(1, -1); 
    '''
    image_vectors = []
    for i in range(0, len(image_matrices)):
        vector = []
        for j in range(0, len(image_matrices[i])):
            for k in range(0, len(image_matrices[i][j])):
                vector.append(image_matrices[i][j][k])
        image_vectors.append(vector)
    
    return image_vectors
    '''
