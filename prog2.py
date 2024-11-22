import numpy as np

# Define prior probabilities
P_A = {"yes": 0.8, "no": 0.2}
P_C = {"yes": 0.5, "no": 0.5}

# Conditional probabilities
P_G_given_A_C = {
    ("Good", "yes", "yes"): 0.9,
    ("Good", "yes", "no"): 0.7,
    ("Good", "no", "yes"): 0.6,
    ("Good", "no", "no"): 0.3,
    ("OK", "yes", "yes"): 0.1,
    ("OK", "yes", "no"): 0.3,
    ("OK", "no", "yes"): 0.4,
    ("OK", "no", "no"): 0.7,
}

P_J_given_G = {"Good": {"yes": 0.8, "no": 0.2}, "OK": {"yes": 0.2, "no": 0.8}}
P_S_given_G = {"Good": {"yes": 0.7, "no": 0.3}, "OK": {"yes": 0.3, "no": 0.7}}

# Monte Carlo Simulation
def monte_carlo_simulation(num_samples=500000, evidence=None):
    """
    Perform Monte Carlo simulation to estimate conditional probabilities in the Bayesian network.

    Args:
        num_samples (int): Number of samples to generate.
        evidence (dict): Evidence variables and their values.

    Returns:
        Estimated probabilities of the target node.
    """
    evidence = evidence or {}
    count_target_given_evidence = 0
    count_evidence = 0

    for _ in range(num_samples):
        # Sample nodes
        A = np.random.choice(["yes", "no"], p=[P_A["yes"], P_A["no"]])
        C = np.random.choice(["yes", "no"], p=[P_C["yes"], P_C["no"]])
        G = np.random.choice(["Good", "OK"], p=[
            P_G_given_A_C[("Good", A, C)],
            P_G_given_A_C[("OK", A, C)],
        ])
        J = np.random.choice(["yes", "no"], p=[
            P_J_given_G[G]["yes"], 
            P_J_given_G[G]["no"]
        ])
        S = np.random.choice(["yes", "no"], p=[
            P_S_given_G[G]["yes"], 
            P_S_given_G[G]["no"]
        ])

        # Store sampled values in a dictionary for evidence matching
        sampled_values = {"A": A, "C": C, "G": G, "J": J, "S": S}

        # Check evidence
        if all(sampled_values[key] == value for key, value in evidence.items()):
            count_evidence += 1
            if G == "Good":  # Target variable
                count_target_given_evidence += 1

    # Avoid division by zero
    if count_evidence == 0:
        return 0

    return count_target_given_evidence / count_evidence

# Example Usage
# Compute P(Good | A=yes, C=yes)
evidence = {"A": "yes", "C": "yes"}
estimated_probability = monte_carlo_simulation(num_samples=500000, evidence=evidence)
print(f"Estimated P(Good | A=yes, C=yes): {estimated_probability}")
