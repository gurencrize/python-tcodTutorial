#型ヒントのサポート
from typing import Optional

import tcod.event

from actions import Action, EscapeAction, MovementAction

# TCODのEventDispatchのサブクラス
class EventHandler(tcod.event.EventDispatch[Action]):
    # EventDispatchにある同名の関数のオーバーライド
    # ×を押した時にプログラムを終了する
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    # キーが押された時に動く
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        # actionのサブクラスが指定された時にそれを保持する
        action: Optional[Action] = None

        key = event.sym

        if key == tcod.event.K_UP:
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = MovementAction(dx=1, dy=0)

        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        # No valid key was pressed
        return action