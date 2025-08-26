sidebar_p = ft.NavigationRail(
        selected_index=0,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.HOUSE_OUTLINED,
                selected_icon=ft.Icons.HOUSE,
                
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.ALBUM_OUTLINED,
                selected_icon=ft.Icons.ALBUM,
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.MUSIC_NOTE_OUTLINED,
                selected_icon=ft.Icons.MUSIC_NOTE
            )
        ],
        on_change=lambda e: navrail_helper(e.control.selected_index)
    )