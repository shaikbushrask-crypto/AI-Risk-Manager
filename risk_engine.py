def calculate_risk_dna(
    amount,
    usual_amount,
    new_device,
    rapid_transactions
):

    score = 0
    reasons = []

    # Spending behavior
    if amount > usual_amount * 3:
        score += 35
        reasons.append(
            "Spending behavior strongly differs from Risk DNA"
        )

    elif amount > usual_amount * 1.5:
        score += 20
        reasons.append(
            "Spending behavior is higher than normal"
        )

    # Device behavior
    if new_device:
        score += 25
        reasons.append(
            "Device behavior differs from normal pattern"
        )

    # Transaction speed
    if rapid_transactions:
        score += 30
        reasons.append(
            "Transaction speed differs from normal pattern"
        )

    # Risk level
    if score >= 70:
        level = "CRITICAL"

    elif score >= 35:
        level = "WARNING"

    else:
        level = "NORMAL"

    return score, level, reasons


def calculate_mutation(dna_score):

    if dna_score >= 70:
        mutation = "CRITICAL CHANGE"

    elif dna_score >= 35:
        mutation = "MAJOR CHANGE"

    elif dna_score >= 20:
        mutation = "SLIGHT CHANGE"

    else:
        mutation = "NORMAL"

    return mutation


def behavioral_mirror(
    amount,
    usual_amount,
    new_device,
    rapid_transactions
):

    mirror = []

    # Spending
    if usual_amount > 0:
        change_percent = (
            (amount - usual_amount) / usual_amount
        ) * 100
    else:
        change_percent = 0

    if amount > usual_amount:
        spending_change = f"+{change_percent:.0f}%"
    else:
        spending_change = f"{change_percent:.0f}%"

    mirror.append({
        "category": "Spending",
        "normal": f"₹{usual_amount:.0f}",
        "current": f"₹{amount:.0f}",
        "change": spending_change
    })

    # Device
    mirror.append({
        "category": "Device",
        "normal": "Trusted Device",
        "current": (
            "New Device"
            if new_device
            else "Trusted Device"
        ),
        "change": (
            "Unusual"
            if new_device
            else "Normal"
        )
    })

    # Transaction speed
    mirror.append({
        "category": "Transaction Speed",
        "normal": "Normal",
        "current": (
            "Rapid"
            if rapid_transactions
            else "Normal"
        ),
        "change": (
            "Unusual"
            if rapid_transactions
            else "Normal"
        )
    })

    return mirror


def counterfactual_risk(
    amount,
    usual_amount,
    new_device,
    rapid_transactions
):

    scenarios = []

    # 1. What if transaction amount was normal?
    normal_amount_score, _, _ = calculate_risk_dna(
        usual_amount,
        usual_amount,
        new_device,
        rapid_transactions
    )

    scenarios.append({
        "scenario": "If transaction amount was normal",
        "score": normal_amount_score
    })

    # 2. What if a trusted device was used?
    trusted_device_score, _, _ = calculate_risk_dna(
        amount,
        usual_amount,
        False,
        rapid_transactions
    )

    scenarios.append({
        "scenario": "If a trusted device was used",
        "score": trusted_device_score
    })

    # 3. What if amount and device were normal?
    normal_behavior_score, _, _ = calculate_risk_dna(
        usual_amount,
        usual_amount,
        False,
        rapid_transactions
    )

    scenarios.append({
        "scenario": "If amount and device were normal",
        "score": normal_behavior_score
    })

    return scenarios


def risk_action(score):

    if score >= 70:
        return "BLOCK / MANUAL REVIEW"

    elif score >= 35:
        return "VERIFY USER"

    else:
        return "ALLOW TRANSACTION"


# STEP 18.4
# Risk Decision Explanation

def risk_explanation(
    score,
    new_device,
    rapid_transactions,
    amount,
    usual_amount
):

    explanations = []

    # Spending explanation
    if amount > usual_amount * 3:
        explanations.append(
            "The transaction amount is significantly higher than the user's normal spending pattern."
        )

    elif amount > usual_amount * 1.5:
        explanations.append(
            "The transaction amount is higher than the user's normal spending pattern."
        )

    # Device explanation
    if new_device:
        explanations.append(
            "The transaction is being performed from a new device instead of a trusted device."
        )

    # Speed explanation
    if rapid_transactions:
        explanations.append(
            "Multiple transactions are occurring at an unusually rapid speed."
        )

    # Final decision explanation
    if score >= 70:
        decision = (
            "Multiple high-risk behavior changes were detected, "
            "so the transaction requires blocking or manual review."
        )

    elif score >= 35:
        decision = (
            "A significant behavioral change was detected, "
            "so the user should be verified before completing the transaction."
        )

    else:
        decision = (
            "The transaction is close to the user's normal behavior, "
            "so it can be allowed."
        )

    return {
        "factors": explanations,
        "decision": decision
    }


# STEP 18.5
# Risk Confidence

def risk_confidence(
    amount,
    usual_amount,
    new_device,
    rapid_transactions
):

    signals = 0

    if amount > usual_amount * 1.5:
        signals += 1

    if new_device:
        signals += 1

    if rapid_transactions:
        signals += 1

    if signals == 3:
        confidence = "HIGH"

    elif signals == 2:
        confidence = "MEDIUM"

    elif signals == 1:
        confidence = "LOW"

    else:
        confidence = "VERY LOW"

    return confidence


# STEP 18.6
# Risk Pattern Classification

def risk_pattern(
    amount,
    usual_amount,
    new_device,
    rapid_transactions
):

    changes = []

    # Spending pattern
    if amount > usual_amount * 3:
        changes.append("HIGH SPENDING CHANGE")

    elif amount > usual_amount * 1.5:
        changes.append("MODERATE SPENDING CHANGE")

    else:
        changes.append("NORMAL SPENDING")

    # Device pattern
    if new_device:
        changes.append("NEW DEVICE")

    else:
        changes.append("TRUSTED DEVICE")

    # Transaction speed pattern
    if rapid_transactions:
        changes.append("RAPID TRANSACTION ACTIVITY")

    else:
        changes.append("NORMAL TRANSACTION SPEED")

    # Overall pattern
    unusual_changes = 0

    if amount > usual_amount * 1.5:
        unusual_changes += 1

    if new_device:
        unusual_changes += 1

    if rapid_transactions:
        unusual_changes += 1

    if unusual_changes == 3:
        pattern = "HIGH-RISK BEHAVIOR PATTERN"

    elif unusual_changes == 2:
        pattern = "SUSPICIOUS BEHAVIOR PATTERN"

    elif unusual_changes == 1:
        pattern = "MINOR BEHAVIOR CHANGE"

    else:
        pattern = "NORMAL BEHAVIOR PATTERN"

    return {
        "overall": pattern,
        "changes": changes
    }


# STEP 18.8
# Risk Trend Analysis

def risk_trend(history):

    if len(history) < 2:
        return "NOT ENOUGH DATA"

    previous_score = history[-2]["score"]
    current_score = history[-1]["score"]

    if current_score > previous_score:
        return "RISK INCREASING"

    elif current_score < previous_score:
        return "RISK DECREASING"

    else:
        return "RISK STABLE"


# STEP 18.9
# Risk Factor Contribution

def risk_factor_contribution(
    amount,
    usual_amount,
    new_device,
    rapid_transactions
):

    factors = []

    # Spending contribution
    if amount > usual_amount * 3:

        factors.append({
            "factor": "Spending",
            "points": 35,
            "reason": (
                "Transaction amount is significantly higher than normal"
            )
        })

    elif amount > usual_amount * 1.5:

        factors.append({
            "factor": "Spending",
            "points": 20,
            "reason": (
                "Transaction amount is higher than normal"
            )
        })

    else:

        factors.append({
            "factor": "Spending",
            "points": 0,
            "reason": (
                "Spending is within normal range"
            )
        })

    # Device contribution
    if new_device:

        factors.append({
            "factor": "New Device",
            "points": 25,
            "reason": (
                "Transaction is from a new device"
            )
        })

    else:

        factors.append({
            "factor": "Device",
            "points": 0,
            "reason": (
                "Trusted device detected"
            )
        })

    # Transaction speed contribution
    if rapid_transactions:

        factors.append({
            "factor": "Rapid Transactions",
            "points": 30,
            "reason": (
                "Transactions are occurring rapidly"
            )
        })

    else:

        factors.append({
            "factor": "Transaction Speed",
            "points": 0,
            "reason": (
                "Transaction speed is normal"
            )
        })

    return factors
# STEP 18.10
# What-If Risk Simulator

def what_if_risk(
    amount,
    usual_amount,
    new_device,
    rapid_transactions
):

    scenarios = []

    # Scenario 1: Current behavior
    current_score, current_level, _ = calculate_risk_dna(
        amount,
        usual_amount,
        new_device,
        rapid_transactions
    )

    scenarios.append({
        "scenario": "Current Behavior",
        "score": current_score,
        "level": current_level
    })

    # Scenario 2: Normal transaction amount
    normal_amount_score, normal_amount_level, _ = calculate_risk_dna(
        usual_amount,
        usual_amount,
        new_device,
        rapid_transactions
    )

    scenarios.append({
        "scenario": "What if amount was normal?",
        "score": normal_amount_score,
        "level": normal_amount_level
    })

    # Scenario 3: Trusted device
    trusted_device_score, trusted_device_level, _ = calculate_risk_dna(
        amount,
        usual_amount,
        False,
        rapid_transactions
    )

    scenarios.append({
        "scenario": "What if trusted device was used?",
        "score": trusted_device_score,
        "level": trusted_device_level
    })

    # Scenario 4: Normal transaction speed
    normal_speed_score, normal_speed_level, _ = calculate_risk_dna(
        amount,
        usual_amount,
        new_device,
        False
    )

    scenarios.append({
        "scenario": "What if transaction speed was normal?",
        "score": normal_speed_score,
        "level": normal_speed_level
    })

    # Scenario 5: Completely normal behavior
    normal_score, normal_level, _ = calculate_risk_dna(
        usual_amount,
        usual_amount,
        False,
        False
    )

    scenarios.append({
        "scenario": "What if all behavior was normal?",
        "score": normal_score,
        "level": normal_level
    })

    return scenarios
# STEP 18.11
# Risk DNA Change Timeline

def risk_change_timeline(history):

    timeline = []

    if not history:
        return timeline

    for i, current in enumerate(history):

        if i == 0:

            timeline.append({
                "analysis": 1,
                "previous_score": None,
                "current_score": current["score"],
                "change": 0,
                "direction": "BASELINE",
                "mutation": current["mutation"]
            })

        else:

            previous = history[i - 1]

            previous_score = previous["score"]
            current_score = current["score"]

            change = current_score - previous_score

            if change > 0:
                direction = "RISK INCREASED"

            elif change < 0:
                direction = "RISK DECREASED"

            else:
                direction = "RISK STABLE"

            timeline.append({
                "analysis": i + 1,
                "previous_score": previous_score,
                "current_score": current_score,
                "change": change,
                "direction": direction,
                "mutation": current["mutation"]
            })

    return timeline
# STEP 18.12
# Risk DNA Fingerprint

def risk_dna_fingerprint(
    amount,
    usual_amount,
    new_device,
    rapid_transactions
):

    # Spending pattern
    if amount > usual_amount * 3:
        spending = "HIGH"
    elif amount > usual_amount * 1.5:
        spending = "MODERATE"
    else:
        spending = "NORMAL"

    # Device pattern
    if new_device:
        device = "NEW"
    else:
        device = "TRUSTED"

    # Transaction speed pattern
    if rapid_transactions:
        speed = "RAPID"
    else:
        speed = "NORMAL"

    # Create unique behavioral fingerprint
    fingerprint = f"{spending}-{device}-{speed}"

    # Overall behavior type
    unusual = 0

    if spending != "NORMAL":
        unusual += 1

    if device == "NEW":
        unusual += 1

    if speed == "RAPID":
        unusual += 1

    if unusual == 3:
        behavior_type = "HIGH-RISK BEHAVIOR PATTERN"

    elif unusual == 2:
        behavior_type = "SUSPICIOUS BEHAVIOR PATTERN"

    elif unusual == 1:
        behavior_type = "MINOR BEHAVIOR CHANGE"

    else:
        behavior_type = "NORMAL BEHAVIOR PATTERN"

    return {
        "spending": spending,
        "device": device,
        "speed": speed,
        "fingerprint": fingerprint,
        "behavior_type": behavior_type
    }
    # STEP 18.13
# Risk DNA Similarity

def risk_dna_similarity(current_fingerprint, previous_fingerprint):

    if not previous_fingerprint:
        return {
            "similarity": 0,
            "level": "BASELINE",
            "changed_components": []
        }

    current_parts = current_fingerprint.split("-")
    previous_parts = previous_fingerprint.split("-")

    changed_components = []

    # Spending comparison
    if current_parts[0] != previous_parts[0]:
        changed_components.append("SPENDING")

    # Device comparison
    if current_parts[1] != previous_parts[1]:
        changed_components.append("DEVICE")

    # Transaction speed comparison
    if current_parts[2] != previous_parts[2]:
        changed_components.append("TRANSACTION SPEED")

    changed = len(changed_components)

    if changed == 0:
        similarity = 100
        level = "VERY HIGH"

    elif changed == 1:
        similarity = 67
        level = "HIGH"

    elif changed == 2:
        similarity = 33
        level = "LOW"

    else:
        similarity = 0
        level = "VERY LOW"

    return {
        "similarity": similarity,
        "level": level,
        "changed_components": changed_components
    }
# ==========================================
# STEP 18.14
# Risk DNA Behavioral Memory
# ==========================================

def risk_dna_memory(
    amount,
    usual_amount,
    new_device,
    rapid_transactions,
    history
):

    # Current behavioral fingerprint
    current_fingerprint = risk_dna_fingerprint(
        amount,
        usual_amount,
        new_device,
        rapid_transactions
    )

    # No previous history
    if not history:
        return {
            "status": "FIRST ANALYSIS",
            "message": (
                "Initial behavioral profile created. "
                "Future transactions will be compared with this baseline."
            ),
            "baseline_fingerprint": current_fingerprint["fingerprint"],
            "previous_analyses": 0,
            "memory_strength": "INITIAL"
        }

    # Collect previous fingerprints
    previous_fingerprints = []

    for item in history:

        if item.get("fingerprint"):

            previous_fingerprints.append(
                item["fingerprint"]["fingerprint"]
            )

    # Count how many times each behavior appeared
    fingerprint_counts = {}

    for fingerprint in previous_fingerprints:

        fingerprint_counts[fingerprint] = (
            fingerprint_counts.get(fingerprint, 0) + 1
        )

    # Find most common historical behavior
    if fingerprint_counts:

        dominant_fingerprint = max(
            fingerprint_counts,
            key=fingerprint_counts.get
        )

        dominant_count = fingerprint_counts[
            dominant_fingerprint
        ]

    else:

        dominant_fingerprint = None
        dominant_count = 0

    # Compare current behavior with dominant memory
    if dominant_fingerprint == current_fingerprint["fingerprint"]:

        status = "BEHAVIOR CONSISTENT"

        message = (
            "Current behavior matches the user's "
            "dominant historical Risk DNA pattern."
        )

    else:

        status = "BEHAVIORAL MEMORY CHANGE"

        message = (
            "Current behavior differs from the user's "
            "dominant historical Risk DNA pattern."
        )

    # Memory strength
    total_analyses = len(previous_fingerprints)

    if total_analyses >= 5:
        memory_strength = "STRONG"

    elif total_analyses >= 3:
        memory_strength = "MEDIUM"

    else:
        memory_strength = "DEVELOPING"

    return {

        "status": status,

        "message": message,

        "current_fingerprint": (
            current_fingerprint["fingerprint"]
        ),

        "dominant_fingerprint": dominant_fingerprint,

        "dominant_count": dominant_count,

        "previous_analyses": total_analyses,

        "memory_strength": memory_strength

    }
# ==========================================
# STEP 18.15
# Risk DNA Evolution Score
# ==========================================

def risk_dna_evolution(
    current_fingerprint,
    previous_fingerprint
):

    # No previous DNA
    if not previous_fingerprint:
        return {
            "evolution_score": 0,
            "change_level": "BASELINE",
            "changed_components": [],
            "message": (
                "This is the first analysis, so no behavioral "
                "evolution can be measured yet."
            )
        }

    current_parts = current_fingerprint.split("-")
    previous_parts = previous_fingerprint.split("-")

    changed_components = []

    # Spending change
    if current_parts[0] != previous_parts[0]:
        changed_components.append("SPENDING")

    # Device change
    if current_parts[1] != previous_parts[1]:
        changed_components.append("DEVICE")

    # Transaction speed change
    if current_parts[2] != previous_parts[2]:
        changed_components.append("TRANSACTION SPEED")

    # Calculate evolution score
    changed = len(changed_components)

    if changed == 0:
        evolution_score = 0
        change_level = "NO CHANGE"

        message = (
            "The user's Risk DNA remains consistent "
            "with the previous behavioral pattern."
        )

    elif changed == 1:
        evolution_score = 33
        change_level = "MINOR EVOLUTION"

        message = (
            "One behavioral component has changed "
            "from the previous Risk DNA."
        )

    elif changed == 2:
        evolution_score = 67
        change_level = "MAJOR EVOLUTION"

        message = (
            "Two behavioral components have changed "
            "from the previous Risk DNA."
        )

    else:
        evolution_score = 100
        change_level = "SIGNIFICANT EVOLUTION"

        message = (
            "All major behavioral components have changed "
            "from the previous Risk DNA."
        )

    return {
        "evolution_score": evolution_score,
        "change_level": change_level,
        "changed_components": changed_components,
        "message": message
    }
# ==========================================
# STEP 18.15
# Risk DNA Evolution Score
# ==========================================

def risk_dna_evolution(
    current_fingerprint,
    previous_fingerprint
):

    if not previous_fingerprint:
        return {
            "evolution_score": 0,
            "change_level": "BASELINE",
            "changed_components": [],
            "message": (
                "This is the first analysis, so no behavioral "
                "evolution can be measured yet."
            )
        }

    current_parts = current_fingerprint.split("-")
    previous_parts = previous_fingerprint.split("-")

    changed_components = []

    if current_parts[0] != previous_parts[0]:
        changed_components.append("SPENDING")

    if current_parts[1] != previous_parts[1]:
        changed_components.append("DEVICE")

    if current_parts[2] != previous_parts[2]:
        changed_components.append("TRANSACTION SPEED")

    changed = len(changed_components)

    if changed == 0:
        evolution_score = 0
        change_level = "NO CHANGE"

        message = (
            "The user's Risk DNA remains consistent "
            "with the previous behavioral pattern."
        )

    elif changed == 1:
        evolution_score = 33
        change_level = "MINOR EVOLUTION"

        message = (
            "One behavioral component has changed "
            "from the previous Risk DNA."
        )

    elif changed == 2:
        evolution_score = 67
        change_level = "MAJOR EVOLUTION"

        message = (
            "Two behavioral components have changed "
            "from the previous Risk DNA."
        )

    else:
        evolution_score = 100
        change_level = "SIGNIFICANT EVOLUTION"

        message = (
            "All major behavioral components have changed "
            "from the previous Risk DNA."
        )

    return {
        "evolution_score": evolution_score,
        "change_level": change_level,
        "changed_components": changed_components,
        "message": message
    }