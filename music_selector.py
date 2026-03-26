class music_selector:
    def __init__(self):
        self.list_of_music = []  # this will consist of genres for users to listen to after putting the appropriate inputs

        # Basic mapping from mood/activity/time_of_day to list of simple music suggestions.
        self._recommendation_rules = {
            ("happy", "study", "morning"): ["Lo-fi Beats", "Chillhop Study Session", "Smooth Jazz", "Acoustic Sunny Vibes"],
            ("happy", "study", "afternoon"): ["Indie Pop Focus", "Light Guitar", "Motivational Piano", "Warm Afternoon Groove"],
            ("happy", "relax", "evening"): ["Coffeehouse Acoustic", "Soft Indie", "Sunset Chill", "Happy Downtempo"],
            ("sad", "relax", "night"): ["Melancholy Piano", "Ambient Rain", "Deep Downtempo", "Reflective Strings"],
            ("energetic", "workout", "morning"): ["Upbeat EDM", "High BPM Pop", "Powerhouse Rock", "Motivational Pump"],
            ("calm", "sleep", "night"): ["Sleepy Ambient", "Spa Meditation", "Nature Soundscapes", "Breathing Music"],
            ("focused", "study", "evening"): ["Minimal Background", "Cinematic Focus", "Drone Study", "Quiet Piano"],
            ("energetic", "commute", "morning"): ["Drive Pop", "Electronic Momentum", "Power Rock", "Jumpstart Beats"],
            ("calm", "relax", "afternoon"): ["Soft Chill", "Nostalgic Lo-fi", "Light Jazz", "Easy Listening"],
            ("sad", "study", "afternoon"): ["Mellow Indie", "Pensive Piano", "Nu Jazz", "Dreamy Instrumental"],
        }

    def select_music(self, mood: str, activity: str, time_of_day: str):
        #lowers all inputs to match
        mood_key = mood.lower().strip()
        activity_key = activity.lower().strip()
        time_key = time_of_day.lower().strip()

        # direct mapping first,
        selected = self._recommendation_rules.get((mood_key, activity_key, time_key))
        if selected:
            self.list_of_music = selected
            return selected

        # v is a list of music suggestions, k is the tuple key (mood, activity, time)
        selected = [v for k, v in self._recommendation_rules.items() if k[0] == mood_key and k[1] == activity_key]
        if selected:
            flattened = [item for sub in selected for item in sub][:8]
            self.list_of_music = flattened
            return flattened 

        selected = [v for k, v in self._recommendation_rules.items() if k[0] == mood_key]
        if selected:
            flattened = [item for sub in selected for item in sub][:8]
            self.list_of_music = flattened
            return flattened

        # final fallback to any available recommendation
        fallback = [item for sub in self._recommendation_rules.values() for item in sub][:8]
        self.list_of_music = fallback
        return fallback
