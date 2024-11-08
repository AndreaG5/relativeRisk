import streamlit as st
import math


# Define the functions
def bayes_posterior(prior_prob, sensitivity):
        prob_congiunta = prior_prob * (1 - sensitivity)
        posterior_prob = prob_congiunta / (prob_congiunta + (1 - prior_prob))
        return posterior_prob


def freq_port(prevalence):
        due_pq = 2 * 1 * math.sqrt(prevalence)
        return due_pq


# Start of Streamlit app
st.title("Bayesian Probability Calculator for Genetic Risk")

# Step 1: Ask if the user knows the prevalence
st.write("Do you know the population prevalence of the disease?")
know_prevalence = st.radio("Choose an option:", ("Yes, I know the prevalence", "No, I need to calculate it"))

# If the user knows the prevalence, use it directly to calculate the posterior probability
if know_prevalence == "Yes, I know the prevalence":
        prevalence = st.number_input("Enter the population prevalence (e.g., 0.05 for 5%):", min_value=0.0, max_value=1.0, step=1e-09)
        sensitivity = st.number_input("Enter the test sensitivity (e.g., 0.90 for 90%):", min_value=0.0, max_value=1.0,step=1e-09)

        # Calculate posterior probability
        if st.button("Calculate Posterior Probability"):
                posterior_prob = bayes_posterior(prevalence, sensitivity)
                st.write(f"The posterior probability of disease given a positive test result is: {posterior_prob:.4f}")

# If the user does not know the prevalence, calculate it first, then use it in the posterior calculation
else:
        input_prevalence = st.number_input("Enter an alternative prevalence value for calculation (e.g., 0.05 for 5%):", min_value=0.0, max_value=1.0, step=1e-09)

        # Calculate frequency-based prevalence using the freq_port function
        if st.button("Calculate Frequency-Based Prevalence"):
                calculated_prevalence = freq_port(input_prevalence)
                st.write(f"The calculated prevalence using frequency method is: {calculated_prevalence:.4f}")

                # Now, use this prevalence to calculate posterior probability
                sensitivity = st.number_input("Enter the test sensitivity for posterior calculation (e.g., 0.90 for 90%):", min_value=0.0,
                                              max_value=1.0, step=1e-09)

                if st.button("Calculate Posterior Probability with Calculated Prevalence"):
                        posterior_prob = bayes_posterior(calculated_prevalence, sensitivity)
                        st.write(f"The posterior probability of disease given a positive test result is: {posterior_prob:.4f}")
