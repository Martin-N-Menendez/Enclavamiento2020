library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity retardador is
	port(
		clk_i: in std_logic;
        rst_i: in std_logic;
        paquete_ok : in std_logic;
        r_data: in std_logic_vector(8-1 downto 0);
        w_data: out std_logic_vector(8-1 downto 0)
	);
    end entity;

architecture Behavioral of retardador is
    
    --type estados_t is (permitido,prohibido);
    --signal estado, estado_siguiente : estados_t;
  
    signal aux_0 : std_logic_vector(8-1 downto 0);
    signal aux_1 : std_logic_vector(8-1 downto 0);
    signal aux_2 : std_logic_vector(8-1 downto 0);
    signal aux_3 : std_logic_vector(8-1 downto 0);
    signal aux_4 : std_logic_vector(8-1 downto 0);
    signal aux_5 : std_logic_vector(8-1 downto 0);
    signal aux_6 : std_logic_vector(8-1 downto 0);
    signal aux_7 : std_logic_vector(8-1 downto 0);
    --signal paquete_aux: std_logic_vector(15-1 downto 0);
    signal ii : integer range 0 to 407 := 0;
    signal jj : integer range 0 to 8 := 0;
    signal kk : integer range 0 to 8 := 0;
    --signal estado : std_logic;
begin    
        
    lectura : process(clk_i)
    begin
        if (clk_i = '1' and clk_i'event) then
            if rst_i = '1' then
                jj <= 0;
                aux_0 <= "00000000";
                aux_1 <= "00000000";
                aux_2 <= "00000000";
                aux_3 <= "00000000";
                aux_4 <= "00000000";
                aux_5 <= "00000000";
                aux_6 <= "00000000";
                aux_7 <= "00000000";
            else          
                if r_data /= "00000000" then
                    
                        case jj is
                            when 0 =>
                                aux_0 <= r_data;
                            when 1 =>
                                aux_1 <= r_data;
                            when 2 =>
                                aux_2 <= r_data;
                            when 3 =>
                                aux_3 <= r_data;
                            when 4 =>
                                aux_4 <= r_data;
                            when 5 =>
                                aux_5 <= r_data;
                            when 6 =>
                                aux_6 <= r_data;
                            when 7 =>
                                aux_7 <= r_data;      
                            when 8 =>
                                jj <= 0;     
                        end case;
                        jj <= jj +1;                    
                end if; 
            end if;
        end if;
    end process;
    
   escritura : process(clk_i) 
   begin 
        if (clk_i = '1' and clk_i'event) then
            if rst_i = '1' then          
                ii <= 0;
                kk <= 0;
            else 
                if ii = 407 then      -- clk 4 ms  -> 32 ms    
                    case kk is
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
                            kk <= 0;     
                    end case;
                    ii <= 0;
                    kk <= kk + 1;             
                else
                    ii <= ii + 1;
                end if;
                
                if kk = 8 then
                    kk <= 0;
                end if;
           
            end if;
        end if;             
    end process;
  
        
end Behavioral;
