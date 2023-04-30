import { Select, Square, Text, VStack } from "@chakra-ui/react";

export default function MidiFader(props: { faderNum: number, layer: string }) {
  let fNum = props.faderNum;
  if (props.layer === "B") {
    fNum = fNum + 1;
  }
  return (
    <VStack>
      <Square size="12" bg="teal">
        <Text>F{props.layer}</Text>
      </Square>
      <Select placeholder="Move Action" size={"xs"}>
        <option value="option1">Option 1</option>
        <option value="option2">Option 2</option>
        <option value="option3">Option 3</option>
      </Select>
    </VStack>
  );
}
