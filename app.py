
from flask import Flask, render_template, request
from statistics import mean, median
import pickle


app = Flask(__name__)


@app.route("/")
def index():

    with open("saved_pkl/poster.pkl","rb") as file:

        poster = pickle.load(file)

    # print(poster['poster'])
    
    with open("saved_pkl/movies.pkl","rb") as file:

        movies = pickle.load(file)

    sorted_movies = sorted(movies['popularity'],reverse=True)

    mData = []
    for idx in sorted_movies[:20]:
        
        # print(idx)
        valls = movies[movies['popularity'] == idx]
        
        dd = valls.iloc[0]

        poster_data = poster[poster['title'] ==  dd['title']]
        # print(poster_data['poster'].iloc[0])

        mData.append({
            'title' : dd['title'],
            'id' : dd['id'],
            'popularity' : dd['popularity'],
            'release_date' : dd['release_date'],
            'vote_average' : dd['vote_average'],
            'vote_count' : dd['vote_count'],
            'poster_img' : poster_data['poster'].iloc[0]
        })


    # for v in mData:

    #     print(v['title'])
        

    return render_template(
        "index.html",
        popular_movies=mData
    )

@app.route("/recommender", methods=["GET","POST"])
def recommender():

    with open("saved_pkl/poster.pkl","rb") as file:

        poster = pickle.load(file)

    with open("saved_pkl/final_movies.pkl","rb") as file:

        final_movies = pickle.load(file)

    C=0
    mList = []
    for val in final_movies['title']:

        if C != 60:
            # print(val)
            mList.append(val)
            C +=1
        else:
            break

    # print(mList)

    
    with open("saved_pkl/similarity.pkl","rb") as file:

        similarity = pickle.load(file)

    Moive_Name =  None
    recomd_data = []
    if request.method == 'POST':
        # Name = request.form["txtName"]
        Name = list(request.form.values())
        Moive_Name = Name[0]

        # print("Hello : " , Name[0])    

        def recomend(movie):
            movie_index = final_movies[final_movies['title'] == movie].index[0]
            dis = similarity[movie_index]
            moives_list = sorted(list(enumerate(dis)),reverse=True,key=lambda x:x[1])[1:6]

            for i in moives_list:
                
                val = [i][0][0]
                poster_data = poster[poster['title'] ==  final_movies.iloc[val].title]

                print(poster_data['poster'].iloc[0])

                recomd_data.append({
                    "title" : final_movies.iloc[val].title,
                    "id" : final_movies.iloc[val].movie_id,
                    "release_date" : final_movies.iloc[val].release_date,
                    "vote_average" : final_movies.iloc[val].vote_average,
                    "vote_count" : final_movies.iloc[val].vote_count,
                    'poster_img' : poster_data['poster'].iloc[0]
                })
                    
                    # final_movies.iloc[val])
                # print(final_movies.iloc[val].title)


        recomend(Name[0])

    # print(recomd_data[0]["id"])
    # for val in recomd_data:
    #     print(val["title"])
    #     print(val["id"])

    return render_template(
        "recommender.html",
        mList=mList,
        recomd_data = recomd_data,
        input_data = Moive_Name 
    )

if __name__ == "__main__":
    app.run(debug=True)
