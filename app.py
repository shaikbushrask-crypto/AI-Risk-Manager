from flask import Flask, render_template, request

from risk_engine import (
    calculate_risk_dna,
    calculate_mutation,
    behavioral_mirror,
    counterfactual_risk,
    risk_action,
    risk_explanation,
    risk_confidence,
    risk_pattern,
    risk_trend,
    risk_factor_contribution,
    what_if_risk,
    risk_change_timeline,
    risk_dna_fingerprint,
    risk_dna_similarity,
    risk_dna_memory,
    risk_dna_evolution
)

app = Flask(__name__)


# ==========================================
# RISK ANALYSIS HISTORY
# ==========================================

history = []


# ==========================================
# HOME ROUTE
# ==========================================

@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        # ==========================================
        # GET USER INPUT
        # ==========================================

        try:
            amount = float(
                request.form.get("amount", 0)
            )

            usual_amount = float(
                request.form.get("usual_amount", 0)
            )

        except (ValueError, TypeError):

            amount = 0
            usual_amount = 0

        new_device = (
            request.form.get("new_device") == "yes"
        )

        rapid_transactions = (
            request.form.get("rapid_transactions") == "yes"
        )


        # ==========================================
        # 1. RISK DNA ANALYSIS
        # ==========================================

        score, level, reasons = calculate_risk_dna(
            amount,
            usual_amount,
            new_device,
            rapid_transactions
        )


        # ==========================================
        # 2. RISK MUTATION
        # ==========================================

        mutation = calculate_mutation(score)


        # ==========================================
        # 3. BEHAVIORAL MIRROR
        # ==========================================

        mirror = behavioral_mirror(
            amount,
            usual_amount,
            new_device,
            rapid_transactions
        )


        # ==========================================
        # 4. COUNTERFACTUAL RISK
        # ==========================================

        counterfactual = counterfactual_risk(
            amount,
            usual_amount,
            new_device,
            rapid_transactions
        )


        # ==========================================
        # 5. RECOMMENDED ACTION
        # ==========================================

        action = risk_action(score)


        # ==========================================
        # 6. RISK DECISION EXPLANATION
        # ==========================================

        explanation = risk_explanation(
            score,
            new_device,
            rapid_transactions,
            amount,
            usual_amount
        )


        # ==========================================
        # 7. RISK CONFIDENCE
        # ==========================================

        confidence = risk_confidence(
            amount,
            usual_amount,
            new_device,
            rapid_transactions
        )


        # ==========================================
        # 8. RISK PATTERN CLASSIFICATION
        # ==========================================

        pattern = risk_pattern(
            amount,
            usual_amount,
            new_device,
            rapid_transactions
        )


        # ==========================================
        # 9. RISK FACTOR CONTRIBUTION
        # ==========================================

        contributions = risk_factor_contribution(
            amount,
            usual_amount,
            new_device,
            rapid_transactions
        )


        # ==========================================
        # 10. RISK DNA FINGERPRINT
        # ==========================================

        fingerprint = risk_dna_fingerprint(
            amount,
            usual_amount,
            new_device,
            rapid_transactions
        )


        # ==========================================
        # 11. RISK DNA SIMILARITY
        # ==========================================

        previous_fingerprint = None

        if len(history) > 0:

            previous_fingerprint = (
                history[-1]["fingerprint"]["fingerprint"]
            )

        dna_similarity = risk_dna_similarity(
            fingerprint["fingerprint"],
            previous_fingerprint
        )


        # ==========================================
        # 12. RISK DNA BEHAVIORAL MEMORY
        # ==========================================
        #
        # Memory is calculated BEFORE saving the
        # current analysis into history.
        #
        # Therefore, it compares the current
        # behavior against previous analyses only.
        #

        dna_memory = risk_dna_memory(
            amount,
            usual_amount,
            new_device,
            rapid_transactions,
            history
        )


        # ==========================================
        # 13. RISK DNA EVOLUTION
        # ==========================================
        #
        # Compare current Risk DNA with the
        # previous Risk DNA.
        #

        previous_evolution_fingerprint = None

        if len(history) > 0:

            previous_evolution_fingerprint = (
                history[-1]["fingerprint"]["fingerprint"]
            )

        dna_evolution = risk_dna_evolution(
            fingerprint["fingerprint"],
            previous_evolution_fingerprint
        )


        # ==========================================
        # 14. SAVE CURRENT ANALYSIS TO HISTORY
        # ==========================================

        history.append({

            "score": score,

            "level": level,

            "mutation": mutation,

            "action": action,

            "confidence": confidence,

            "fingerprint": fingerprint

        })


        # ==========================================
        # 15. RISK TREND
        # ==========================================

        trend = risk_trend(history)


        # ==========================================
        # 16. WHAT-IF RISK SIMULATOR
        # ==========================================

        what_if = what_if_risk(
            amount,
            usual_amount,
            new_device,
            rapid_transactions
        )


        # ==========================================
        # 17. RISK DNA CHANGE TIMELINE
        # ==========================================

        timeline = risk_change_timeline(history)


        # ==========================================
        # FINAL RESULT
        # ==========================================

        result = {

            # --------------------------------------
            # Basic Risk DNA
            # --------------------------------------

            "score": score,

            "level": level,

            "mutation": mutation,


            # --------------------------------------
            # Recommended Action
            # --------------------------------------

            "action": action,


            # --------------------------------------
            # Risk Intelligence
            # --------------------------------------

            "confidence": confidence,

            "pattern": pattern,

            "contributions": contributions,


            # --------------------------------------
            # Behavioral Analysis
            # --------------------------------------

            "mirror": mirror,

            "counterfactual": counterfactual,


            # --------------------------------------
            # Explanation
            # --------------------------------------

            "explanation": explanation,


            # --------------------------------------
            # Risk Trend
            # --------------------------------------

            "trend": trend,


            # --------------------------------------
            # What-If Risk Simulator
            # --------------------------------------

            "what_if": what_if,


            # --------------------------------------
            # Risk DNA Timeline
            # --------------------------------------

            "timeline": timeline,


            # --------------------------------------
            # Risk DNA Fingerprint
            # --------------------------------------

            "fingerprint": fingerprint,


            # --------------------------------------
            # Risk DNA Similarity
            # --------------------------------------

            "dna_similarity": dna_similarity,


            # --------------------------------------
            # Risk DNA Behavioral Memory
            # --------------------------------------

            "dna_memory": dna_memory,


            # --------------------------------------
            # Risk DNA Evolution
            # --------------------------------------

            "dna_evolution": dna_evolution,


            # --------------------------------------
            # Behavior Changes
            # --------------------------------------

            "reasons": reasons

        }


    # ==========================================
    # RENDER HTML
    # ==========================================

    return render_template(
        "index.html",
        result=result,
        history=history
    )


# ==========================================
# START FLASK APPLICATION
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)