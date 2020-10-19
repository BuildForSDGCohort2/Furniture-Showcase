import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, View, Text, SafeAreaView, Button, Alert, Platform, Dimensions } from 'react-native';
import { useDimensions, useDeviceOrientation } from '@react-native-community/hooks' ;
export default function App() {

  // console.log(useDimensions());
  console.log(useDeviceOrientation());
  return (
    <SafeAreaView style={styles.container}>
      <button>Chaguo Lako</button>
      {/* <Image source={{ uri: "https://raw.githubusercontent.com/l-mwarangu/image/main/oie_Ump4SElbr93U.png" }}/> */}
      <View style={{
        backgroundColor: "blue",
        width: '50%',
        height: 70,
      }}></View>
      <Button 
        title="Log in" 
        // onPress={()}
        color="brown"
        
        />
      <StatusBar style="auto" />
    </SafeAreaView>
  );
}
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    paddingTop: Platform.OS === "android" ? statusBar.currentHeight  : 0 ,   // alignItems: 'center',
    // justifyContent: 'center',
  },
});
