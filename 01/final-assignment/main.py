import utils as u

def assign_candidates_to_stations(stations, candidates):
    assignments_dic = {}
    candidates_assigned = set()

    while len(assignments_dic) < len(stations):
        any_assignments = False

        for station, qualification in stations:
            if station in assignments_dic:
                continue

            best_match = None
            most_experience = -1

            for candidate in candidates:
                name, qual, experience = candidate
                if name not in candidates_assigned and qual == qualification:
                    if experience > most_experience:
                        most_experience = experience
                        best_match = name

            if best_match:
                assignments_dic[station] = best_match
                candidates_assigned.add(best_match)
                any_assignments = True

        if not any_assignments:
            break
    return assignments_dic

assignments = assign_candidates_to_stations(u.stations, u.candidates)
for station, candidate in assignments.items():
    print(f"{station}: {candidate}")