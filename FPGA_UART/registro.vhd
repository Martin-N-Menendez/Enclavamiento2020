library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity registro is
	port(
		clk_i: in std_logic;
        rst_i: in std_logic;
        paquete_ok : in std_logic;
        paquete_i: in std_logic_vector(15-1 downto 0);
        w_data: out std_logic_vector(8-1 downto 0)
	);
    end entity;

architecture Behavioral of registro is
    
    --type estados_t is (permitido,prohibido);
    --signal estado, estado_siguiente : estados_t;
  
   --signal char_data : std_logic_vector(8-1 downto 0);
    signal paquete_aux: std_logic_vector(15-1 downto 0);
    signal nuevo : std_logic;
    signal nuevo_aux : std_logic;

    signal aux_0 : std_logic_vector(8-1 downto 0);
    signal aux_1 : std_logic_vector(8-1 downto 0);
    signal aux_2 : std_logic_vector(8-1 downto 0);
    signal aux_3 : std_logic_vector(8-1 downto 0);
    signal aux_4 : std_logic_vector(8-1 downto 0);
    signal aux_5 : std_logic_vector(8-1 downto 0);
    signal aux_6 : std_logic_vector(8-1 downto 0);
    signal aux_7 : std_logic_vector(8-1 downto 0);
    signal aux_8 : std_logic_vector(8-1 downto 0);
    signal aux_9 : std_logic_vector(8-1 downto 0);
    signal aux_10 : std_logic_vector(8-1 downto 0);
    signal aux_11 : std_logic_vector(8-1 downto 0);
    signal aux_12 : std_logic_vector(8-1 downto 0);
    signal aux_13 : std_logic_vector(8-1 downto 0);
    signal aux_14 : std_logic_vector(8-1 downto 0);

    signal pulsos : integer range 0 to 407 := 0;
    signal leidos : integer range 0 to 15 := 0;
    signal escritos : integer range 0 to 16 := 0;
    signal contador : integer range 0 to 15 := 0;
begin    
    
    lectura : process(clk_i)
    begin
        if (clk_i = '1' and clk_i'event) then
            if rst_i = '1' then
                leidos <= 0;
                aux_0  <= "00000000";
                aux_1  <= "00000000";
                aux_2  <= "00000000";
                aux_3  <= "00000000";
                aux_4  <= "00000000";
                aux_5  <= "00000000";
                aux_6  <= "00000000";
                aux_7  <= "00000000";
                aux_8  <= "00000000";
                aux_9  <= "00000000";
                aux_10 <= "00000000";
                aux_11 <= "00000000";
                aux_12 <= "00000000";
                aux_13 <= "00000000";
                aux_14 <= "00000000";
            else          
                if paquete_i /= "000000000000000" and nuevo = '1' then       
                        case leidos is
                            when 0 =>
                                if paquete_i(14-leidos) = '0' then
                                    aux_0 <= "00110010";
                                end if;
                                if paquete_i(14-leidos) = '1' then
                                    aux_0 <= "00110001";
                                end if;
                            when 1 =>
                                if paquete_i(14-leidos) = '0' then
                                    aux_1 <= "00110010";
                                end if;
                                if paquete_i(14-leidos) = '1' then
                                    aux_1 <= "00110001";
                                end if;
                            when 2 =>
                                if paquete_i(14-leidos) = '0' then
                                    aux_2 <= "00110010";
                                end if;
                                if paquete_i(14-leidos) = '1' then
                                    aux_2 <= "00110001";
                                end if;
                            when 3 =>
                                if paquete_i(14-leidos) = '0' then
                                    aux_3 <= "00110010";
                                end if;
                                if paquete_i(14-leidos) = '1' then
                                    aux_3 <= "00110001";
                                end if;
                            when 4 =>
                                if paquete_i(14-leidos) = '0' then
                                    aux_4 <= "00110010";
                                end if;
                                if paquete_i(14-leidos) = '1' then
                                    aux_4 <= "00110001";
                                end if;
                            when 5 =>
                                if paquete_i(14-leidos) = '0' then
                                    aux_5 <= "00110010";
                                end if;
                                if paquete_i(14-leidos) = '1' then
                                    aux_5 <= "00110001";
                                end if;
                            when 6 =>
                                if paquete_i(14-leidos) = '0' then
                                    aux_6 <= "00110010";
                                end if;
                                if paquete_i(14-leidos) = '1' then
                                    aux_6 <= "00110001";
                                end if;
                            when 7 =>
                                if paquete_i(14-leidos) = '0' then
                                    aux_7 <= "00110010";
                                end if;
                                if paquete_i(14-leidos) = '1' then
                                    aux_7 <= "00110001";
                                end if;
                            when 8 =>
                                if paquete_i(14-leidos) = '0' then
                                    aux_8 <= "00110010";
                                end if;
                                if paquete_i(14-leidos) = '1' then
                                    aux_8 <= "00110001";
                                end if;
                            when 9 =>
                                if paquete_i(14-leidos) = '0' then
                                    aux_9 <= "00110010";
                                end if;
                                if paquete_i(14-leidos) = '1' then
                                    aux_9 <= "00110001";
                                end if;
                            when 10 =>
                                if paquete_i(14-leidos) = '0' then
                                    aux_10 <= "00110010";
                                end if;
                                if paquete_i(14-leidos) = '1' then
                                    aux_10 <= "00110001";
                                end if;
                            when 11 =>
                                if paquete_i(14-leidos) = '0' then
                                    aux_11 <= "00110010";
                                end if;
                                if paquete_i(14-leidos) = '1' then
                                    aux_11 <= "00110001";
                                end if;
                            when 12 =>
                                if paquete_i(14-leidos) = '0' then
                                    aux_12 <= "00110010";
                                end if;
                                if paquete_i(14-leidos) = '1' then
                                    aux_12 <= "00110001";
                                end if;
                            when 13 =>
                                if paquete_i(14-leidos) = '0' then
                                    aux_13 <= "00110010";
                                end if;
                                if paquete_i(14-leidos) = '1' then
                                    aux_13 <= "00110001";
                                end if;
                            when 14 =>
                                if paquete_i(14-leidos) = '0' then
                                    aux_14 <= "00110010";
                                end if;
                                if paquete_i(14-leidos) = '1' then
                                    aux_14 <= "00110001";
                                end if;    
                            when 15 =>
                                leidos <= 0;     
                        end case;
                        if leidos < 15 then
                            leidos <= leidos + 1; 
                        end if;                   
                end if; 
                if leidos = 15 then
                    leidos <= 0;
                end if;
                if nuevo = '0' then
                    leidos <= 0;
                end if;
            end if;
        end if;
    end process;
    
   escritura : process(clk_i) 
   begin 
        if (clk_i = '1' and clk_i'event) then
            if rst_i = '1' then          
                pulsos <= 0;
                escritos <= 0;
                w_data <= "00000000";
            else 
                
                if nuevo_aux /= nuevo then
                    pulsos <= 0;
                end if;
                nuevo_aux <= nuevo; 
                    
                if pulsos = 407 then      -- clk 4 ms  -> 32 ms    
                    case escritos is
                        when 0 =>
                            w_data <= aux_0;
                        when 1 =>
                            w_data <= aux_1;
                        when 2 =>
                            w_data <= aux_2;
                        when 3 =>
                            w_data <= aux_3;
                        when 4 =>
                            w_data <= aux_4;
                        when 5 =>
                            w_data <= aux_5;
                        when 6 =>
                            w_data <= aux_6;
                        when 7 =>
                            w_data <= aux_7; 
                        when 8 =>
                            w_data <= aux_8; 
                        when 9 =>
                            w_data <= aux_9; 
                        when 10 =>
                            w_data <= aux_10; 
                        when 11 =>
                            w_data <= aux_11; 
                        when 12 =>
                            w_data <= aux_12; 
                        when 13 =>
                            w_data <= aux_13; 
                        when 14 =>
                            w_data <= aux_14; 
                        when 15 => null;     
                        when 16 => 
                            escritos <= 0;     
                    end case;
                    pulsos <= 0;
                    escritos <= escritos + 1;    
    
                else   
                    if nuevo = '1' then
                        pulsos <= pulsos + 1;
                    end if;
                end if;
                
                if escritos = 16 then
                    escritos <= 0;
                    w_data <= "00000000";
                end if;
           
            end if;
        end if;             
    end process;
       
   habilitador : process(clk_i) 
   begin 
        if (clk_i = '1' and clk_i'event) then
            if rst_i = '1' then          
                nuevo <= '0'; 
            else        
                
                if paquete_aux /= paquete_i then
                    --pulsos <= 0; 
                    nuevo <= '1';
                end if;
                paquete_aux <= paquete_i;
                
                if paquete_ok = '1' then
                    nuevo <= '1';
                end if;
                if escritos = 16 then
                    nuevo <= '0';
                end if;
                       
            end if;
        end if;             
    end process;
        
end Behavioral;
