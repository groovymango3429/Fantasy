#!/usr/bin/env python3
"""
Validation script for NFL Fantasy Playoff Rosters
Ensures all rosters meet league requirements and no player is used twice
"""

def validate_rosters():
    # Define all rosters
    rosters = {
        "Week 1 - Wild Card": {
            "QB": ["Justin Herbert"],
            "RB": ["Najee Harris", "Jaylen Warren"],
            "WR": ["Keenan Allen", "George Pickens", "Quentin Johnston"],
            "TE": ["Pat Freiermuth"],
            "PK": ["Cameron Dicker"],
            "DEF": ["Denver Broncos"]
        },
        "Week 2 - Divisional": {
            "QB": ["Jalen Hurts"],
            "RB": ["Kyren Williams", "D'Andre Swift"],
            "WR": ["A.J. Brown", "Cooper Kupp", "DeVonta Smith"],
            "TE": ["Dalton Kincaid", "Tyler Higbee"],
            "PK": [],
            "DEF": ["Buffalo Bills"]
        },
        "Week 3 - Conference": {
            "QB": ["Lamar Jackson"],
            "RB": ["Derrick Henry", "Jahmyr Gibbs", "David Montgomery"],
            "WR": ["Zay Flowers", "Amon-Ra St. Brown", "Jameson Williams"],
            "TE": ["Mark Andrews"],
            "PK": [],
            "DEF": ["Baltimore Ravens"]
        },
        "Week 4 - Super Bowl": {
            "QB": ["Patrick Mahomes"],
            "RB": ["Isiah Pacheco", "Kareem Hunt"],
            "WR": ["Xavier Worthy", "JuJu Smith-Schuster", "Skyy Moore"],
            "TE": ["Travis Kelce"],
            "PK": ["Harrison Butker"],
            "DEF": ["Kansas City Chiefs"]
        }
    }
    
    # Position requirements
    requirements = {
        "QB": (1, 1),    # exactly 1
        "RB": (2, 3),    # 2-3
        "WR": (2, 3),    # 2-3
        "TE": (1, 2),    # 1-2
        "PK": (0, 1),    # 0-1
        "DEF": (0, 1)    # 0-1
    }
    
    all_valid = True
    all_players = []
    
    print("=" * 60)
    print("FANTASY PLAYOFF ROSTER VALIDATION")
    print("=" * 60)
    print()
    
    # Validate each week
    for week, roster in rosters.items():
        print(f"\n{week}:")
        print("-" * 40)
        
        total_players = 0
        week_valid = True
        
        # Check position requirements
        for position, (min_req, max_req) in requirements.items():
            count = len(roster[position])
            total_players += count
            
            status = "✓" if min_req <= count <= max_req else "✗"
            print(f"  {position}: {count} players (req: {min_req}-{max_req}) {status}")
            
            if not (min_req <= count <= max_req):
                week_valid = False
            
            # Add players to all_players list
            all_players.extend(roster[position])
        
        # Check total players
        total_status = "✓" if total_players == 9 else "✗"
        print(f"  TOTAL: {total_players} players (req: 9) {total_status}")
        
        if total_players != 9:
            week_valid = False
        
        if not week_valid:
            all_valid = False
            print(f"  ⚠️  Week FAILED validation")
        else:
            print(f"  ✓ Week PASSED validation")
    
    # Check for duplicate players across weeks
    print("\n" + "=" * 60)
    print("DUPLICATE PLAYER CHECK")
    print("=" * 60)
    
    player_count = {}
    for player in all_players:
        player_count[player] = player_count.get(player, 0) + 1
    
    duplicates_found = False
    for player, count in player_count.items():
        if count > 1:
            print(f"  ✗ {player} used {count} times!")
            duplicates_found = True
    
    if not duplicates_found:
        print("  ✓ No duplicate players found!")
        print(f"  ✓ Total unique players: {len(all_players)}")
    else:
        all_valid = False
    
    # Final result
    print("\n" + "=" * 60)
    print("FINAL VALIDATION RESULT")
    print("=" * 60)
    
    if all_valid:
        print("  ✓✓✓ ALL ROSTERS VALID ✓✓✓")
        print("  Ready for playoff competition!")
        return 0
    else:
        print("  ✗✗✗ VALIDATION FAILED ✗✗✗")
        print("  Please fix errors above")
        return 1

if __name__ == "__main__":
    exit(validate_rosters())
