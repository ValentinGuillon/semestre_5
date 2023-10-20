open Mips
open Mips_helper

let () = 
    print_asm Stdlib.stdout
        {
            text = 
                def "main"
                    (
                        [ Li (T0, 1) ]
                      @ [ Li (T1, 2147483648) ]
                      @ loop (LessThan (T0, T1)) 
                            (
                                [ Move (T2, T0) ]
                              @ loop (LessThanZero T2)
                                    (
                                        [ Li (T3, 1) ]
                                      @ [ And (T4, T2, T3) ]
                                      @ branch (NotEqual (T4, Zero))
                                            ( print_str "diez" )
                                            ( print_str "space" )
                                      @ [ Srl (T2, T2, 1) ]
                                    )
                              @ print_str "nl"
                              @ [ Sll (T3, T0, 1) ]
                              @ [ Xor (T0, T0, T3) ]
                            )
                      @ print_str "aled"
                    )
        ;   data = [
                ("nl", Asciiz "\n")
            ;   ("space", Asciiz " ")
            ;   ("diez", Asciiz "#")
            ;   ("aled", Asciiz "ez mdr\n")
            ]
        }
;;


