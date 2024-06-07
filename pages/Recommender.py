import pandas as pd
import streamlit as st
import pickle

st.set_page_config(page_title='Recommend Apartments')

# Load the data and cosine similarity matrices
with open('location_distance.pkl', 'rb') as file:
    df = pickle.load(file)
with open('cosine_sim1.pkl', 'rb') as file:
    cosine_sim1 = pickle.load(file)
with open('cosine_sim2.pkl', 'rb') as file:
    cosine_sim2 = pickle.load(file)
with open('cosine_sim3.pkl', 'rb') as file:
    cosine_sim3 = pickle.load(file)


def recommend_properties_with_scores(property_name, top_n=5):
    cosine_sim_matrix = 30 * cosine_sim1 + 20 * cosine_sim2 + 8 * cosine_sim3
    # Get the similarity scores for the property using its name as the index
    sim_scores = list(enumerate(cosine_sim_matrix[df.index.get_loc(property_name)]))
    # Sort properties based on the similarity scores
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    # Get the indices and scores of the top_n most similar properties
    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]
    # Retrieve the names of the top properties using the indices
    top_properties = df.index[top_indices].tolist()
    # Create a dataframe with the results
    recommendations_df = pd.DataFrame({
        'PropertyName': top_properties,
    })
    return recommendations_df


st.title('Recommend Apartments')
apartment_name = st.selectbox('Select an apartment', sorted(df.index.to_list()))

if st.button('Recommend'):
    recommendation = recommend_properties_with_scores(apartment_name)
    apartment = pd.read_csv('apartments.csv')
    merged_df = recommendation.merge(apartment[['PropertyName', 'Link']], on='PropertyName', how='left')
    merged_df['Link'] = merged_df['Link'].apply(lambda x: f'[Link]({x})')
    st.markdown(merged_df.to_markdown(index=False))
