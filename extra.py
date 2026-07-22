# import pickle

# with open("saved_pkl/final_movies.pkl","rb") as file:

#     final_movies = pickle.load(file)


# with open("saved_pkl/similarity.pkl","rb") as file:

#     similarity = pickle.load(file)

# def recomend(movie):
#     movie_index = final_movies[final_movies['title'] == movie].index[0]
#     dis = similarity[movie_index]
#     moives_list = sorted(list(enumerate(dis)),reverse=True,key=lambda x:x[1])[1:6]

#     for i in moives_list:
        
#         val = [i][0][0]
#         print(final_movies.iloc[val].title)


# recomend('Avatar')


# ----------------------------

# with open("saved_pkl/movies.pkl","rb") as file:

#     movies = pickle.load(file)

# sorted_movies = sorted(movies['popularity'],reverse=True)

# mData = []
# for idx in sorted_movies[:10]:
    
#     # print(idx)
#     valls = movies[movies['popularity'] == idx]
    
#     dd = valls.iloc[0]
#     # print(dd['title'])
#     mData.append({
#         'title' : dd['title'],
#         'id' : dd['id'],
#         'popularity' : dd['popularity'],
#         'release_date' : dd['release_date'],
#         'vote_average' : dd['vote_average']
#     })


# for v in mData:

#     print(v)

