import { useState } from "react";
// import { invoke } from "@tauri-apps/api/tauri";
// import { emit, listen } from "@tauri-apps/api/event";
import {
  Box,
  Button,
  Center,
  HStack,
  Text,
  useColorModeValue,
  VStack,
} from "@chakra-ui/react";
import Nav from "./components/Navbar";
import MidiEncoder from "./components/controls/MidiEncoder";
import MidiButton from "./components/controls/MidiButton";
import MidiFader from "./components/controls/MidiFader";

function App() {
  // const [greetMsg, setGreetMsg] = useState("");
  // const [name, setName] = useState("");
  // const { colorMode, toggleColorMode } = useColorMode();
  const [layer, setLayer] = useState("A");


  return (
    <Box h={"100vh"} w={"100%"}>
      <Nav />
      <Box h={"60vh"}>
        <Center h={"100%"}>
          <Box
            // h={"85%"}
            // w={"95%"}
            bg={useColorModeValue("gray.100", "gray.900")}
            borderRadius={20}
            p={4}
          >
            <HStack>
              <VStack spacing={4}>
                <HStack spacing={4}>
                  <MidiEncoder encoderNum={1} layer={layer} />
                  <MidiEncoder encoderNum={2} layer={layer} />
                  <MidiEncoder encoderNum={3} layer={layer} />
                  <MidiEncoder encoderNum={4} layer={layer} />
                  <MidiEncoder encoderNum={5} layer={layer} />
                  <MidiEncoder encoderNum={6} layer={layer} />
                  <MidiEncoder encoderNum={7} layer={layer} />
                  <MidiEncoder encoderNum={8} layer={layer} />
                </HStack>
                <HStack spacing={4}>
                  <MidiButton buttonNum={1} layer={layer} />
                  <MidiButton buttonNum={2} layer={layer} />
                  <MidiButton buttonNum={3} layer={layer} />
                  <MidiButton buttonNum={4} layer={layer} />
                  <MidiButton buttonNum={5} layer={layer} />
                  <MidiButton buttonNum={6} layer={layer} />
                  <MidiButton buttonNum={7} layer={layer} />
                  <MidiButton buttonNum={8} layer={layer} />
                </HStack>
                <HStack spacing={4}>
                  <MidiButton buttonNum={9} layer={layer} />
                  <MidiButton buttonNum={10} layer={layer} />
                  <MidiButton buttonNum={11} layer={layer} />
                  <MidiButton buttonNum={12} layer={layer} />
                  <MidiButton buttonNum={13} layer={layer} />
                  <MidiButton buttonNum={14} layer={layer} />
                  <MidiButton buttonNum={15} layer={layer} />
                  <MidiButton buttonNum={16} layer={layer} />
                </HStack>
              </VStack>
              <VStack spacing={20}>
                <MidiFader faderNum={1} layer={layer} />
                <VStack>
                  <Text fontSize={"md"}>Layer {layer}</Text>
                  <Button
                    size={"sm"}
                    onClick={() => {
                      switch (layer) {
                        case "A":
                          setLayer("B");
                          break;
                        case "B":
                          setLayer("A");
                          break;
                        default:
                          setLayer("A");
                          break;
                      }
                    }}
                  >
                    Change Layer
                  </Button>
                </VStack>
              </VStack>
            </HStack>
          </Box>
        </Center>
      </Box>
    </Box>
  );
}

export default App;
