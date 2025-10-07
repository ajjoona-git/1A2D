def time_to_int(time):
    hour, minute = map(int, time.split(':'))
    return hour * 60 + minute

def replace_note(melody):
    melody = melody.replace('C#', 'c')
    melody = melody.replace('D#', 'd')
    melody = melody.replace('F#', 'f')
    melody = melody.replace('G#', 'g')
    melody = melody.replace('A#', 'a')
    melody = melody.replace('B#', 'b')
    melody = melody.replace('E#', 'e')
    return melody

def solution(m, musicinfos):
    # 재생된 멜로디를 딕셔너리 형태로 저장한다.
    playedmusics = {}
    for i in range(len(musicinfos)):
        start, end, title, melody = musicinfos[i].split(',')
        start = time_to_int(start)
        end = time_to_int(end)
        played_time = end - start
        
        melody = replace_note(melody)
        index = 0

        played_melody = ""
        for _ in range(played_time):
            played_melody += melody[index]
            index = (index + 1) % len(melody)

        playedmusics[i] = {
            'title': title,
            'played': played_time,
            'melody': played_melody,
        }

    # 재생된 시간이 긴 음악 제목 순서대로 정렬한다.
    sorted_playedmusics = sorted(
        playedmusics.items(), 
        key=lambda x: (x[1]['played'], -x[0]), 
        reverse=True
    )

    # 일치하는 멜로디를 찾는다.
    for _, value in sorted_playedmusics:
        m = replace_note(m)
        if m in value['melody']:
            return value['title']
    
    return "(None)"